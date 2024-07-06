import { InputText } from "primereact/inputtext"
import { useState } from "react"
import { Checkbox } from 'primereact/checkbox'
import { Button } from 'primereact/button'
import { Link } from 'react-router-dom'
function Parsy(){
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
                <Button><Link to="/">переход</Link></Button>
            </>
        )
}
export {Parsy}