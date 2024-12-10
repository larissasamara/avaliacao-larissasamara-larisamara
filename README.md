
# Sistema de Gerenciamento de Atendimentos

Este projeto é um sistema para gerenciar atendimentos realizados por profissionais de saúde, pacientes e convênios, com informações detalhadas sobre os atendimentos, diagnósticos e tipos de atendimento.

## Modelo de Dados

O modelo de dados é estruturado para fornecer uma visão clara e organizada das entidades principais do sistema e seus relacionamentos.

---

### **Tabela: Profissional**
Representa os profissionais responsáveis pelos atendimentos.

| Atributo        | Tipo         | Descrição                                    |
|------------------|--------------|---------------------------------------------|
| `id`            | `AutoField`  | Identificador único do profissional.        |
| `nome`          | `CharField`  | Nome do profissional (máx. 100 caracteres). |
| `sobrenome`     | `CharField`  | Sobrenome do profissional (máx. 100 caracteres). |
| `especialidade` | `CharField`  | Área de atuação do profissional.            |

---

### **Tabela: Paciente**
Armazena informações sobre os pacientes.

| Atributo        | Tipo         | Descrição                                    |
|------------------|--------------|---------------------------------------------|
| `id`            | `AutoField`  | Identificador único do paciente.            |
| `nome`          | `CharField`  | Nome do paciente (máx. 100 caracteres).     |
| `sobrenome`     | `CharField`  | Sobrenome do paciente (máx. 100 caracteres).|
| `data_nascimento` | `DateField` | Data de nascimento do paciente.            |
| `telefone`      | `CharField`  | Telefone para contato (opcional).           |
| `endereco`      | `TextField`  | Endereço completo do paciente (opcional).   |

---

### **Tabela: Convenio**
Representa os convênios médicos associados ao atendimento.

| Atributo        | Tipo         | Descrição                                    |
|------------------|--------------|---------------------------------------------|
| `id`            | `AutoField`  | Identificador único do convênio.            |
| `nome`          | `CharField`  | Nome do convênio (máx. 100 caracteres).     |
| `descricao`     | `TextField`  | Informações adicionais sobre o convênio.    |

---

### **Tabela: Diagnostico**
Armazena informações sobre diagnósticos.

| Atributo        | Tipo         | Descrição                                    |
|------------------|--------------|---------------------------------------------|
| `id`            | `AutoField`  | Identificador único do diagnóstico.         |
| `descricao`     | `CharField`  | Descrição do diagnóstico (máx. 255 caracteres). |

---

### **Tabela: Atendimento**
Modelo central que conecta profissionais, pacientes, convênios e diagnósticos.

| Atributo        | Tipo         | Descrição                                    |
|------------------|--------------|---------------------------------------------|
| `id`            | `AutoField`  | Identificador único do atendimento.         |
| `profissional`  | `ForeignKey` | Referência ao **Profissional** responsável pelo atendimento. |
| `paciente`      | `ForeignKey` | Referência ao **Paciente** que recebeu o atendimento. |
| `data_atendimento` | `DateTimeField` | Data e hora do atendimento.               |
| `convenio`      | `ForeignKey` | (Opcional) Referência ao **Convenio** utilizado. |
| `tipo_atendimento` | `CharField` | Tipo do atendimento (consulta, exame, terapia). |
| `diagnostico`   | `ForeignKey` | (Opcional) Referência ao **Diagnostico** associado. |
| `observacoes`   | `TextField`  | Notas adicionais sobre o atendimento.       |

---

## Relacionamentos

- **Atendimento** possui:
  - Um **Profissional** associado (obrigatório).
  - Um **Paciente** associado (obrigatório).
  - Um **Convenio** associado (opcional).
  - Um **Diagnostico** associado (opcional).

- **Profissional** e **Paciente** podem estar vinculados a múltiplos atendimentos (relação 1:N).

- **Convenio** pode estar vinculado a múltiplos atendimentos (relação 1:N).

- **Diagnostico** pode ser usado em múltiplos atendimentos (relação 1:N).

---

## Exemplo de Uso

- **Consulta por profissional**: Obter todos os atendimentos realizados por um profissional específico.
- **Consulta por paciente**: Listar todos os atendimentos de um paciente.
- **Consulta por período**: Filtrar atendimentos realizados dentro de um intervalo de datas.
- **Consulta por convênio**: Analisar o uso de convênios em atendimentos.
- **Consulta por tipo de atendimento**: Classificar atendimentos por categorias.
- **Consulta por diagnóstico**: Agrupar atendimentos com base nos diagnósticos realizados.

---

## Configuração

Certifique-se de aplicar as migrações para criar as tabelas no banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```