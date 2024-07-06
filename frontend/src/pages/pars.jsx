import { InputText } from "primereact/inputtext"
import { useState } from "react"
import { Checkbox } from 'primereact/checkbox'
import { Button } from 'primereact/button'
import { Card } from 'primereact/card'
import { Link } from 'react-router-dom'
import { DataView, DataViewLayoutOptions } from 'primereact/dataview'
import { useNavigate } from 'react-router-dom';

function Parsy(){
    const [pusto, setPusto] = useState(false)
    const navigate = useNavigate();
    const [data, setData] = useState([])
    const [city, setCity] = useState("")
    const [salary, setSalary] = useState("")
    const [employment, setEmployment] = useState("")
    function onEmploymentChange(value){
        if(value == employment){
            setEmployment("")
        }else{
            setEmployment(value)
        }
    }
    function Params_db(){
        let link='http://127.0.0.1:8000/vacancies/params'
        if(city.length!=0||salary.length!=0||employment!=0){
            link+="?"
        }
        if(city.length!=0){
            link+="city="+city+"&"
        }
        if(salary.length!=0){
            link+="salary="+salary+"&"
        }
        if(employment!=0){
            link+="employment="+employment+"&"
        }


        fetch(link)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            setData(data);
            console.log(data)
            if(data.length==0){
                setPusto(true)
            }else{
                setPusto(false)
            }
        })
        .catch((error) => {
            console.log(error)
          });

    }
    const itemTemplate = (item) => {
        return(
            <Card title={item.name}>
                <p className="m-0"></p>
                <p>Город: {item.city}</p>
                <p>{item.experience}</p>
                <p>{item.employment}</p>
                <p>{item.requirement}</p>
                <p>Обязанности: {item.responsibility}</p>
                <p>Зарплата: {item.salary}</p>
                <p>Для лучшего ознакомления перейдите по ссылке: </p> <Link to={item.link}>{item.link}</Link>

            </Card>

        )
    }
    return(
            <>
                <InputText className="p-inputtext-lg" placeholder="Введите город" value={city} onChange={(e) => setCity(e.target.value)} /> 
                <InputText className="p-inputtext-lg" placeholder="Введите зарплату" value={salary} onChange={(e) => setSalary(e.target.value)} /> 
                <div className="flex flex-wrap justify-content-center gap-3">
                    <div className="flex align-items-center">
                        <Checkbox onChange={() => onEmploymentChange("Полная занятость")} checked={employment=="Полная занятость"} />
                        <label className="ml-2">Полная занятость</label>
                    </div>
                    <div className="flex align-items-center">
                        <Checkbox onChange={() => onEmploymentChange("Частичная занятость")} checked={employment=="Частичная занятость"} />
                        <label className="ml-2">Частичная занятость</label>
                    </div>
                    <div className="flex align-items-center">
                        <Checkbox onChange={() => onEmploymentChange("Стажировка")} checked={employment=="Стажировка"} />
                        <label className="ml-2">Стажировка</label>
                    </div>
                </div>
                <Button label="Посмотреть результат" onClick={Params_db}/> 
                <Button onClick={() => navigate('/')}>Переход</Button>
                {pusto?<p>Нет таких вакансий</p>:<></>}
                <DataView value={data} itemTemplate={itemTemplate} />
                
            </>
        )
}
export {Parsy}