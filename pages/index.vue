<template>
  <v-layout
    column
    justify-center
    align-center>
    
    <v-flex
      xs12
      sm8
      md6>
      <v-card>
             <v-card-title>
          <div>
            <span class="red--text">Legende:</span><br>
            <span>J:  Le cours est disponible Jour seulement</span><br>
            <span>S:  Le cours est disponible le soir seulement</span><br>
            <span>JS:  Le cours est disponible jour et soir</span><br>
            <span>*:  La disponibilité n'est pas assuré</span><br>
          </div>
        </v-card-title>
          </v-card>
      <div class="text-xs-center">
           <v-container fluid>
    <v-layout row wrap align-center>
      <v-flex xs6>
        <v-subheader>Choisir le programmme pour voir la liste des cours</v-subheader>
      </v-flex>

      <v-flex xs6>
        <v-select
          v-model="select"
          :hint="`${select.programme}, ${select.abbr}`"
          :items="items"
          item-text="programme"
          item-value="abbr"
          label="Select"
          persistent-hint
          return-object
          single-line
          v-on:change="updateTable"
        ></v-select>
      </v-flex>
    </v-layout>
  </v-container>
        <v-data-table
            :headers="headers"
            :items="shownCourses"
            hide-actions
            class="elevation-1"
          >
            <template slot="headerCell" slot-scope="props">
              <v-tooltip bottom>
                <span slot="activator">
                  {{ props.header.text }}
                </span>
                <span>
                  {{ props.header.text }}
                </span>
              </v-tooltip>
            </template>
            <template slot="items" slot-scope="props">
              <td>{{ props.item.name }}</td>
              <td class="text-xs-right">{{ props.item.sigle }}</td>
              <td class="text-xs-right">{{ props.item.session1 }}</td>
              <td class="text-xs-right">{{ props.item.session2 }}</td>
              <td class="text-xs-right">{{ props.item.session3 }}</td>
              <td class="text-xs-right">{{ props.item.session4 }}</td>
              <td class="text-xs-right">{{ props.item.session5 }}</td>
            </template>
          </v-data-table>

      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from 'axios'
export default {
  components: {},
  data() {
    return {
        select: { programme: 'Cours Généraux', abbr: 'SEG' },
        items: [
          { programme: 'Cours Généraux', abbr: 'SEG'},
          { programme: 'Génie logiciel et TI', abbr: 'LOGTI'},
          { programme: 'Génie Électrique', abbr: 'ELE'},
          { programme: 'Génie Mecanique', abbr: 'MEC'},
          { programme: 'Génie des opérations logistique', abbr: 'GOL'},
          { programme: 'Génie de la prodution automatisée', abbr: 'GPA'},
          { programme: 'Génie de la constructions', abbr: 'CTN'}

        ],
      headers: [
        {
          text: "Cours",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Sigle", value: "sigle" },
        { text: "Hiver 2019", value: "session1" },
        { text: "Été 2019", value: "session2" },
        { text: "Automne 2019", value: "session3" },
        { text: "Hiver 2020", value: "session4" },
        { text: "Été 2020", value: "session5" }
      ],
      shownCourses: [],
      logCourses: [],
      eleCourses: [],
      segCourses: [],
      mecCourses: [],
      golCourses: [],
      ctnCourses: [],
      gpaCourses: [],
      links :{ 
          LOG: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/LOG.json',
          SEG: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/SEG.json',
          ELE: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/ELE.json',
          MEC: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/MEC.json',
          GPA: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/GPA.json',
          GOL: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/GOL.json',
          CTN: 'https://github.com/jalilbengoufa/ETSParcours/blob/master/json_files/CTN.json',
    
        }
    };
  },
  async created() {
        var self = this;
        self.getCourses(self);
  },
  methods: {
    
    async getCourses(self){
       return axios.get(self.links.SEG)
          .then((res) => {
            self.shownCourses = res.data
            self.segCourses = res.data
       });
    },
    updateTable(source){
        var self = this;
        if(source.abbr == 'SEG'){
            self.shownCourses = self.segCourses
        }
        if(source.abbr == 'LOGTI'){
            if(self.logCourses.length == 0){
                axios.get(self.links.LOG)
                    .then((res) => {
                    self.logCourses = res.data;
                });
            }else{
                self.shownCourses = self.logCourses
            }  
        }
        if(source.abbr == 'ELE'){
            if(self.eleCourses.length == 0){
                 axios.get(self.links.ELE)
                .then((res) => {
                    self.eleCourses = res.data;
                    self.shownCourses = res.data;
                });
             }else{
                self.shownCourses = self.eleCourses
             }
        }
        if(source.abbr == 'MEC'){
            if(self.mecCourses.length == 0){
                 axios.get(self.links.MEC)
                .then((res) => {
                    self.mecCourses = res.data;
                    self.shownCourses = res.data;
                });
             }else{
                self.shownCourses = self.mecCourses
             }
        }
        if(source.abbr == 'CTN'){
            if(self.ctnCourses.length == 0){
                 axios.get(self.links.CTN)
                .then((res) => {
                    self.ctnCourses = res.data;
                    self.shownCourses = res.data;
                });
             }else{
                self.shownCourses = self.ctnCourses
             }
        }
        if(source.abbr == 'GPA'){
            if(self.gpaCourses.length == 0){
                 axios.get(self.links.GPA)
                .then((res) => {
                    self.gpaCourses = res.data;
                    self.shownCourses = res.data;
                });
             }else{
                self.shownCourses = self.gpaCourses
             }
        }
        if(source.abbr == 'GOL'){
            if(self.golCourses.length == 0){
                 axios.get(self.links.GOL)
                .then((res) => {
                    self.golCourses = res.data;
                    self.shownCourses = res.data;
                });
             }else{
                self.shownCourses = self.golCourses
             }
        }
    }
  }

};
</script>
