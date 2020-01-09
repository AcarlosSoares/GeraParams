pessoa = {
1 : {'nome' : 'Joao', 'idade' : '23', 'sexo' : 'M'},
2 : {'nome' : 'Jose', 'idade' : '12', 'sexo' : 'M'},
3 : {'nome' : 'Maria', 'idade' : '35', 'sexo' : 'F'},
4 : {'nome' : 'Pedro', 'idade' : '51', 'sexo' : 'M'}
}

lista = []
for k, v in pessoa.items():
  print(v)
  lista.append(v)

for k, v in pessoa.items():
  print(v)
  lista.append(v)

print(pessoa[1])
print(pessoa[2])


    {% for lista_item in lista %}
    {% for k, list in lista_item.items %}

      <tr>
        <td style="vertical-align:middle">{{ list.atributo }}</td>
        <td style="vertical-align:middle">{{ list.pk }}</td>
        <td style="vertical-align:middle">{{ list.inc }}</td>
        <td style="vertical-align:middle">{{ list.alt }}</td>
        <td style="vertical-align:middle">{{ list.exc }}</td>
        <td style="vertical-align:middle">{{ list.tipo }}</td>
        <td style="vertical-align:middle">{{ list.titulo }}</td>
        <td style="vertical-align:middle">{{ list.tam_bd }}</td>
        <td style="vertical-align:middle">{{ list.tam_lista }}</td>
        <td style="vertical-align:middle">{{ list.tam_relat }}</td>
        <td class="text-center center-align">

          <a href="{{ url_for('delete', val=list.atributo) }}" class="btn btn-ligth btn-sm" role="button" title="Alterar Dados">
            <i class="material-icons cor-azul" style="vertical-align:middle;">delete</i>
          </a>

        </td>
      </tr>

    {% endfor %}
    {% endfor %}
