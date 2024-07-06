import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Data from './Data';
import Vacancies from './Vacancies'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={Vacancies} />
        <Route path="/data" Component={Data} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
