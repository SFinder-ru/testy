import { useState } from 'react';
import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Divider,
  Grid,
  TextField
} from '@material-ui/core';

const states = [
  {
    value: 'front-end',
    label: 'Front-end'
  },
  {
    value: 'back-end',
    label: 'Back-end'
  },
  {
    value: 'full-stack',
    label: 'Full-stack'
  },
  {
    value: 'android developer',
    label: 'Android Developer'
  },
  {
    value: 'ios developer',
    label: 'IOS Developer'
  }
];
const languages = [
  {
    value: 'django',
    label: 'Django'
  },
  {
    value: 'c#',
    label: 'C#'
  },
  {
    value: 'react',
    label: 'React'
  },
  {
    value: 'c++',
    label: 'c++'
  },
  {
    value: 'java',
    label: 'Java'
  }
];

const AccountProfileDetails = (props) => {
  const [values, setValues] = useState({
    firstName: 'Михаил',
    lastName: 'Бабухин',
    email: 'mbabukhin@gmail.com',
    phone: '79197125282',
    state: 'Frontend',
    language: 'ХЗ'
  });

  const handleChange = (event) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value
    });
  };

  return (
    <form
      autoComplete="off"
      noValidate
      {...props}
    >
      <Card>
        <CardHeader
          subheader="Информацию можно изменить"
          title="Профиль"
        />
        <Divider />
        <CardContent>
          <Grid
            container
            spacing={3}
          >
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                helperText="Пожалуйста, укажите как вас зовут"
                label="Ваше имя"
                name="firstName"
                onChange={handleChange}
                required
                value={values.firstName}
                variant="outlined"
              />
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Ваша фамилия"
                name="lastName"
                onChange={handleChange}
                required
                value={values.lastName}
                variant="outlined"
              />
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Ваша почта"
                name="email"
                onChange={handleChange}
                required
                value={values.email}
                variant="outlined"
              />
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Ваш номер"
                name="phone"
                onChange={handleChange}
                type="number"
                value={values.phone}
                variant="outlined"
              />
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Выбирите языки-технологии"
                name="language"
                onChange={handleChange}
                required
                select
                SelectProps={{ native: true }}
                value={values.language}
                variant="outlined"
              >
                {languages.map((option) => (
                  <option
                    key={option.value}
                    value={option.value}
                  >
                    {option.label}
                  </option>
                ))}
              </TextField>
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Выбирите направление"
                name="state"
                onChange={handleChange}
                required
                select
                SelectProps={{ native: true }}
                value={values.state}
                variant="outlined"
              >
                {states.map((option) => (
                  <option
                    key={option.value}
                    value={option.value}
                  >
                    {option.label}
                  </option>
                ))}
              </TextField>
            </Grid>
          </Grid>
        </CardContent>
        <Divider />
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'flex-end',
            p: 2
          }}
        >
          <Button
            color="primary"
            variant="contained"
          >
            Сохранить изменения
          </Button>
        </Box>
      </Card>
    </form>
  );
};

export default AccountProfileDetails;
