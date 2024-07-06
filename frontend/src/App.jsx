import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Vacancy } from './pages/vacancy'
import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import "primereact/resources/themes/soho-light/theme.css";
import { Routes, Route } from 'react-router-dom'
import { Parsy } from './pages/pars'

function App() {
  const [count, setCount] = useState(0)

  return (
    <PrimeReactProvider>
        <Routes>
          <Route index element={< Vacancy/>} />
          <Route exact path="vacancy_parser" element={< Parsy/>} />
        </Routes>
    </PrimeReactProvider>
  )
}

export default App
