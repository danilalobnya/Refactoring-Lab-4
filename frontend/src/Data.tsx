import React, { ChangeEventHandler, FormEvent, useEffect, useState } from 'react';
import axios from 'axios';
import background from './images/background.jpg';
import './Data.css';

interface Vacancies {
  id: number;
  url: string;
  title: string;
  responsibilities: string;
  requirements: string;
  company_name: string;
}

function Data() {
  const [vacancies, setVacancies] = useState<Vacancies[]>([]);

  useEffect(() => {
    const fetchVacancies = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/vacancies'); // Замените на ваш адрес сервера
        setVacancies(response.data);
      } catch (error) {
        console.error('Ошибка при получении данных:', error);
      }
    };

    fetchVacancies();
  }, []);


  const [filterTitle, setFilterTitle] = useState('');
  const [filterCompany, setFilterCompany] = useState('');
  const [filterRequirements, setFilterRequirements] = useState('');


  const handleFilterTitleChange: ChangeEventHandler<HTMLInputElement> = (event) => {
    setFilterTitle(event.target.value);
  };

  const handleFilterCompanyChange: ChangeEventHandler<HTMLInputElement> = (event) => {
    setFilterCompany(event.target.value);
  };

  const handleFilterRequirementsChange: ChangeEventHandler<HTMLInputElement> = (event) => {
    setFilterRequirements(event.target.value);
  };

  // Функция для фильтрации вакансий
  const filteredVacancies = vacancies.filter((vacancy) => {
    return (
      (filterTitle === '' || vacancy.title.toLowerCase().includes(filterTitle.toLowerCase())) &&
      (filterCompany === '' || vacancy.company_name.toLowerCase().includes(filterCompany.toLowerCase())) &&
      (filterRequirements === '' || vacancy.requirements.toLowerCase().includes(filterRequirements.toLowerCase()))
    );
  });


  return (
    <div className='body'>
      <p className='filter-text'>Фильтр по названию работы</p>
      <input className='filter' type="text" value={filterTitle} onChange={handleFilterTitleChange}></input>
      <p className='filter-text'>Фильтр по названию компании</p>
      <input className='filter' type="text" value={filterCompany} onChange={handleFilterCompanyChange}></input>
      <p className='filter-text'>Фильтр по требованиям</p>
      <input className='filter' type="text" value={filterRequirements} onChange={handleFilterRequirementsChange}></input>
      <img className='background' src={background} alt="Background" />
      <table className='table'>
        <thead>
          <tr className='table-th'>
            <th className='table-th'>Название работы</th>
            <th className='table-th'>Ссылка на вакансию</th>
            <th className='table-th'>Требования</th>
            <th className='table-th'>Обязанности</th>
            <th className='table-th'>Название компании</th>
          </tr>
        </thead>
        <tbody>
          {filteredVacancies.map((vacancy) => (
            <tr key={vacancy.id}>
              <td className='table-td'>{vacancy.title}</td>
              <td className='table-td'><a href={vacancy.url} target="_blank" rel="noopener noreferrer">{vacancy.url}</a></td>
              <td className='table-td'>{vacancy.requirements}</td>
              <td className='table-td'>{vacancy.responsibilities}</td>
              <td className='table-td'>{vacancy.company_name}</td>
            </tr>
          ))};
        </tbody>
      </table>
    </div>
  );
}

export default Data;
