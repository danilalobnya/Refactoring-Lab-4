import React, { useState } from 'react';
import './Vacancies.css';
import background from './images/background.jpg';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


interface EmploymentOption {
  id: string;
  name: string;
}

type ChangeEvent = React.ChangeEvent<HTMLSelectElement | HTMLInputElement>;

function Vacancies() {

  const navigate = useNavigate();

  const navigateToData = () => {
    navigate('/data');
  };

  const [experience, setExperience] = useState('noExperience');
  const [schedule, setSchedule] = useState('fullDay');
  const [area, setArea] = useState(1);
  const [searchText, setSearchText] = useState<string>(''); // Добавлено состояние для текста поиска

  const handleExperienceChange = (event: ChangeEvent) => {
    setExperience(event.target.value);
  };

  const handleScheduleChange = (event: ChangeEvent) => {
    setSchedule(event.target.value);
  };

  const handleAreaChange = (event: ChangeEvent) => {
    setArea(Number(event.target.value));
  };

  const handleSearchTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchText(event.target.value); // Обновление состояния при изменении текста
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/add_search_parameters', {
        text: searchText,
        experience: experience,
        schedule: schedule,
        area: area
      });
      console.log(response.data);
      navigateToData();
    } catch (error) {
      console.error('Ошибка при отправке данных:', error);
    }
  };

  return (
    <div className="App">
      <img className='background' src={background} alt="Фон"/>
      <div className='vacancies'>ВАКАНСИИ</div>
      <input
        className='vacanciesInput'
        type='text'
        value={searchText}
        onChange={handleSearchTextChange} // Добавлен обработчик изменения
      />
      <p className='experience'>ОПЫТ</p>
      <select className='experienceSelect' value={experience} onChange={handleExperienceChange}>
      <option value="any">Неважно</option>
        <option value="noExperience">Нет опыта</option>
        <option value="between1And3">От 1 года до 3 лет</option>
        <option value="between3And6">От 3 до 6 лет</option>
        <option value="moreThan6">Более 6 лет</option>
      </select>
      <p className='schedule'>ГРАФИК</p>
      <select className='scheduleSelect' value={schedule} onChange={handleScheduleChange}>
      <option value="any">Неважно</option>
        <option value="fullDay">Полный день</option>
        <option value="shift">Сменный график</option>
        <option value="flexible">Гибкий график</option>
        <option value="remote">Удаленная работа</option>
        <option value="flyInFlyOut">Вахтовый метод</option>
      </select>
      <p className='area'>ГОРОД</p>
      <select className='areaSelect' value={area} onChange={handleAreaChange}>
      <option value="any">Неважно</option>
        <option value="1">Москва</option>
        <option value="2">Санкт-Петербург</option>
      </select>
      <button className='button' onClick={handleSubmit}>ПОЛУЧИТЬ ИНФОРМАЦИЮ</button>
      <div className='info'>ПАРСЕР ВАКАНСИЙ С САЙТА HH.RU</div>
    </div>
  );
};

export default Vacancies;
