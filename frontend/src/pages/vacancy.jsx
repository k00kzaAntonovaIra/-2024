import { useState } from "react"
import { InputText } from "primereact/inputtext"
import { Checkbox } from 'primereact/checkbox'
import { DataView, DataViewLayoutOptions } from 'primereact/dataview'
import { Button } from 'primereact/button'
import { Card } from 'primereact/card'
import { Link } from 'react-router-dom'
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';



function Vacancy( ){
    const navigate = useNavigate();
    const [data, setData] = useState([])
    const [text, setText] = useState("")
    const [experience, setExperience] = useState("")
    function onExperienceChange(value){
        if(value == experience){
            setExperience("")
        }else{
            setExperience(value)
        }
    }
    function Vacancy_db(){
        let link='http://127.0.0.1:8000/vacancy'
        if(text.length!=0||experience.length!=0){
            link+="?"
        }
        if(text.length!=0){
            link+="text="+text+"&"
        }
        if(experience!=0){
            link+="experience="+experience+"&"
        }

        fetch(link)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            setData(data);
            console.log(data)
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
    useEffect(() => {
        fetch("http://127.0.0.1:8000")
          .then((response) => response.json())
          .catch((error) => console.log(error));
      }, []);
 
    return(
        <>
            {/* <p>{employment}</p> */}

            <InputText className="p-inputtext-lg" placeholder="Введите вакансию" value={text} onChange={(e) => setText(e.target.value)} />
        
            <div className="flex flex-wrap justify-content-center gap-3">
                <div className="flex align-items-center">
                    <Checkbox onChange={() => onExperienceChange("noExperience")} checked={experience=="noExperience"} />
                    <label className="ml-2">Нет опыта</label>
                </div>
                <div className="flex align-items-center">
                    <Checkbox onChange={() => onExperienceChange("between1And3")} checked={experience=="between1And3"} />
                    <label className="ml-2">От 1 года до 3 лет</label>
                </div>
                <div className="flex align-items-center">
                    <Checkbox onChange={() => onExperienceChange("between3And6")} checked={experience=="between3And6"} />
                    <label className="ml-2">От 3 до 6 лет</label>
                </div>
                <div className="flex align-items-center">
                    <Checkbox onChange={() => onExperienceChange("moreThan6")} checked={experience=="moreThan6"} />
                    <label className="ml-2">Более 6 лет</label>
                </div>
            </div>
            <Button label="Посмотреть результат" onClick={Vacancy_db}/>
            <Button onClick={() => navigate('/vacancy_parser')}>Переход</Button>
            <DataView value={data} itemTemplate={itemTemplate} />
            

        </>
    )

}
export {Vacancy}