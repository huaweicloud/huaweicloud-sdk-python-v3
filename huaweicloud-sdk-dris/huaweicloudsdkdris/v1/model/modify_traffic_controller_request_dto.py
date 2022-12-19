# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTrafficControllerRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'lat': 'float',
        'lon': 'float',
        'ele': 'float',
        'pos_description': 'str',
        'installation_mode': 'str',
        'road_name': 'str',
        'link_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon',
        'ele': 'ele',
        'pos_description': 'pos_description',
        'installation_mode': 'installation_mode',
        'road_name': 'road_name',
        'link_id': 'link_id'
    }

    def __init__(self, name=None, description=None, lat=None, lon=None, ele=None, pos_description=None, installation_mode=None, road_name=None, link_id=None):
        """ModifyTrafficControllerRequestDTO

        The model defined in huaweicloud sdk

        :param name: **参数说明**：名称。  **取值范围**：长度不超过128，只允许汉字、字母、数字、以及_-等字符的组合。 
        :type name: str
        :param description: **参数说明**：描述
        :type description: str
        :param lat: **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。
        :type lat: float
        :param lon: **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。
        :type lon: float
        :param ele: **参数说明**：定义海拔高程，可选，单位为分米。
        :type ele: float
        :param pos_description: **参数说明**：位置说明。  **取值范围**：长度不超过128，只允许字母、数字、以及_等字符的组合。 
        :type pos_description: str
        :param installation_mode: **参数说明**：架设方式。  **取值范围**： - columnar：柱式 - road-side-attach：路侧附着式 - cantilever：悬臂式 - gantry：门架式 - lane-above-attach：车行道上方附着式\&quot; 
        :type installation_mode: str
        :param road_name: **参数说明**：所属道路名称，比如高速名称。  **取值范围**：长度不超过64，只允许汉字、字母、数字、以及_-等字符的组合。 
        :type road_name: str
        :param link_id: **参数说明**：信号机设备所属路段ID。  **取值范围**：长度等于30，只允许大写字母、数字。 
        :type link_id: str
        """
        
        

        self._name = None
        self._description = None
        self._lat = None
        self._lon = None
        self._ele = None
        self._pos_description = None
        self._installation_mode = None
        self._road_name = None
        self._link_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon
        if ele is not None:
            self.ele = ele
        if pos_description is not None:
            self.pos_description = pos_description
        if installation_mode is not None:
            self.installation_mode = installation_mode
        if road_name is not None:
            self.road_name = road_name
        if link_id is not None:
            self.link_id = link_id

    @property
    def name(self):
        """Gets the name of this ModifyTrafficControllerRequestDTO.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许汉字、字母、数字、以及_-等字符的组合。 

        :return: The name of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyTrafficControllerRequestDTO.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许汉字、字母、数字、以及_-等字符的组合。 

        :param name: The name of this ModifyTrafficControllerRequestDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyTrafficControllerRequestDTO.

        **参数说明**：描述

        :return: The description of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyTrafficControllerRequestDTO.

        **参数说明**：描述

        :param description: The description of this ModifyTrafficControllerRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def lat(self):
        """Gets the lat of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。

        :return: The lat of this ModifyTrafficControllerRequestDTO.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。

        :param lat: The lat of this ModifyTrafficControllerRequestDTO.
        :type lat: float
        """
        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。

        :return: The lon of this ModifyTrafficControllerRequestDTO.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。

        :param lon: The lon of this ModifyTrafficControllerRequestDTO.
        :type lon: float
        """
        self._lon = lon

    @property
    def ele(self):
        """Gets the ele of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义海拔高程，可选，单位为分米。

        :return: The ele of this ModifyTrafficControllerRequestDTO.
        :rtype: float
        """
        return self._ele

    @ele.setter
    def ele(self, ele):
        """Sets the ele of this ModifyTrafficControllerRequestDTO.

        **参数说明**：定义海拔高程，可选，单位为分米。

        :param ele: The ele of this ModifyTrafficControllerRequestDTO.
        :type ele: float
        """
        self._ele = ele

    @property
    def pos_description(self):
        """Gets the pos_description of this ModifyTrafficControllerRequestDTO.

        **参数说明**：位置说明。  **取值范围**：长度不超过128，只允许字母、数字、以及_等字符的组合。 

        :return: The pos_description of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._pos_description

    @pos_description.setter
    def pos_description(self, pos_description):
        """Sets the pos_description of this ModifyTrafficControllerRequestDTO.

        **参数说明**：位置说明。  **取值范围**：长度不超过128，只允许字母、数字、以及_等字符的组合。 

        :param pos_description: The pos_description of this ModifyTrafficControllerRequestDTO.
        :type pos_description: str
        """
        self._pos_description = pos_description

    @property
    def installation_mode(self):
        """Gets the installation_mode of this ModifyTrafficControllerRequestDTO.

        **参数说明**：架设方式。  **取值范围**： - columnar：柱式 - road-side-attach：路侧附着式 - cantilever：悬臂式 - gantry：门架式 - lane-above-attach：车行道上方附着式\" 

        :return: The installation_mode of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._installation_mode

    @installation_mode.setter
    def installation_mode(self, installation_mode):
        """Sets the installation_mode of this ModifyTrafficControllerRequestDTO.

        **参数说明**：架设方式。  **取值范围**： - columnar：柱式 - road-side-attach：路侧附着式 - cantilever：悬臂式 - gantry：门架式 - lane-above-attach：车行道上方附着式\" 

        :param installation_mode: The installation_mode of this ModifyTrafficControllerRequestDTO.
        :type installation_mode: str
        """
        self._installation_mode = installation_mode

    @property
    def road_name(self):
        """Gets the road_name of this ModifyTrafficControllerRequestDTO.

        **参数说明**：所属道路名称，比如高速名称。  **取值范围**：长度不超过64，只允许汉字、字母、数字、以及_-等字符的组合。 

        :return: The road_name of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._road_name

    @road_name.setter
    def road_name(self, road_name):
        """Sets the road_name of this ModifyTrafficControllerRequestDTO.

        **参数说明**：所属道路名称，比如高速名称。  **取值范围**：长度不超过64，只允许汉字、字母、数字、以及_-等字符的组合。 

        :param road_name: The road_name of this ModifyTrafficControllerRequestDTO.
        :type road_name: str
        """
        self._road_name = road_name

    @property
    def link_id(self):
        """Gets the link_id of this ModifyTrafficControllerRequestDTO.

        **参数说明**：信号机设备所属路段ID。  **取值范围**：长度等于30，只允许大写字母、数字。 

        :return: The link_id of this ModifyTrafficControllerRequestDTO.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this ModifyTrafficControllerRequestDTO.

        **参数说明**：信号机设备所属路段ID。  **取值范围**：长度等于30，只允许大写字母、数字。 

        :param link_id: The link_id of this ModifyTrafficControllerRequestDTO.
        :type link_id: str
        """
        self._link_id = link_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyTrafficControllerRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
