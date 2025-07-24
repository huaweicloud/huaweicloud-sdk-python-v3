# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Drive:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'manufacturer': 'str',
        'model': 'str',
        'serial_number': 'str',
        'revision': 'str',
        'media_type': 'str',
        'protocol': 'str',
        'sas_address': 'str',
        'capacity_bytes': 'int',
        'capable_speed_gbs': 'int',
        'negotiated_speed_gbs': 'int',
        'hotspare_type': 'str',
        'hours_of_powered_up': 'int',
        'power_state': 'str',
        'patrol_state': 'str',
        'associated_resource': 'str',
        'predicted_media_life_left_percent': 'int',
        'health': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'serial_number': 'serial_number',
        'revision': 'revision',
        'media_type': 'media_type',
        'protocol': 'protocol',
        'sas_address': 'sas_address',
        'capacity_bytes': 'capacity_bytes',
        'capable_speed_gbs': 'capable_speed_gbs',
        'negotiated_speed_gbs': 'negotiated_speed_gbs',
        'hotspare_type': 'hotspare_type',
        'hours_of_powered_up': 'hours_of_powered_up',
        'power_state': 'power_state',
        'patrol_state': 'patrol_state',
        'associated_resource': 'associated_resource',
        'predicted_media_life_left_percent': 'predicted_media_life_left_percent',
        'health': 'health'
    }

    def __init__(self, id=None, name=None, manufacturer=None, model=None, serial_number=None, revision=None, media_type=None, protocol=None, sas_address=None, capacity_bytes=None, capable_speed_gbs=None, negotiated_speed_gbs=None, hotspare_type=None, hours_of_powered_up=None, power_state=None, patrol_state=None, associated_resource=None, predicted_media_life_left_percent=None, health=None):
        r"""Drive

        The model defined in huaweicloud sdk

        :param id: 驱动器资源的ID
        :type id: str
        :param name: 驱动器资源的名称
        :type name: str
        :param manufacturer: 驱动器的制造商
        :type manufacturer: str
        :param model: 驱动器型号
        :type model: str
        :param serial_number: 驱动器的序列号
        :type serial_number: str
        :param revision: 驱动器的版本信息
        :type revision: str
        :param media_type: 驱动器的介质类型
        :type media_type: str
        :param protocol: 驱动器遵从的协议
        :type protocol: str
        :param sas_address: SAS地址
        :type sas_address: str
        :param capacity_bytes: 容量（单位：byte）
        :type capacity_bytes: int
        :param capable_speed_gbs: 驱动器接口的最大速率（单位：Gbps）
        :type capable_speed_gbs: int
        :param negotiated_speed_gbs: 驱动器接口的协商速率（单位：Gbps）
        :type negotiated_speed_gbs: int
        :param hotspare_type: 驱动器的热备状态
        :type hotspare_type: str
        :param hours_of_powered_up: 驱动器上电运行时间（单位：h）
        :type hours_of_powered_up: int
        :param power_state: 驱动器电源状态
        :type power_state: str
        :param patrol_state: 驱动器巡检状态
        :type patrol_state: str
        :param associated_resource: 驱动器的资源归属
        :type associated_resource: str
        :param predicted_media_life_left_percent: 驱动器的剩余寿命百分比
        :type predicted_media_life_left_percent: int
        :param health: 健康状态
        :type health: str
        """
        
        

        self._id = None
        self._name = None
        self._manufacturer = None
        self._model = None
        self._serial_number = None
        self._revision = None
        self._media_type = None
        self._protocol = None
        self._sas_address = None
        self._capacity_bytes = None
        self._capable_speed_gbs = None
        self._negotiated_speed_gbs = None
        self._hotspare_type = None
        self._hours_of_powered_up = None
        self._power_state = None
        self._patrol_state = None
        self._associated_resource = None
        self._predicted_media_life_left_percent = None
        self._health = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if serial_number is not None:
            self.serial_number = serial_number
        if revision is not None:
            self.revision = revision
        if media_type is not None:
            self.media_type = media_type
        if protocol is not None:
            self.protocol = protocol
        if sas_address is not None:
            self.sas_address = sas_address
        if capacity_bytes is not None:
            self.capacity_bytes = capacity_bytes
        if capable_speed_gbs is not None:
            self.capable_speed_gbs = capable_speed_gbs
        if negotiated_speed_gbs is not None:
            self.negotiated_speed_gbs = negotiated_speed_gbs
        if hotspare_type is not None:
            self.hotspare_type = hotspare_type
        if hours_of_powered_up is not None:
            self.hours_of_powered_up = hours_of_powered_up
        if power_state is not None:
            self.power_state = power_state
        if patrol_state is not None:
            self.patrol_state = patrol_state
        if associated_resource is not None:
            self.associated_resource = associated_resource
        if predicted_media_life_left_percent is not None:
            self.predicted_media_life_left_percent = predicted_media_life_left_percent
        if health is not None:
            self.health = health

    @property
    def id(self):
        r"""Gets the id of this Drive.

        驱动器资源的ID

        :return: The id of this Drive.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Drive.

        驱动器资源的ID

        :param id: The id of this Drive.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Drive.

        驱动器资源的名称

        :return: The name of this Drive.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Drive.

        驱动器资源的名称

        :param name: The name of this Drive.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this Drive.

        驱动器的制造商

        :return: The manufacturer of this Drive.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this Drive.

        驱动器的制造商

        :param manufacturer: The manufacturer of this Drive.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def model(self):
        r"""Gets the model of this Drive.

        驱动器型号

        :return: The model of this Drive.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this Drive.

        驱动器型号

        :param model: The model of this Drive.
        :type model: str
        """
        self._model = model

    @property
    def serial_number(self):
        r"""Gets the serial_number of this Drive.

        驱动器的序列号

        :return: The serial_number of this Drive.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this Drive.

        驱动器的序列号

        :param serial_number: The serial_number of this Drive.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def revision(self):
        r"""Gets the revision of this Drive.

        驱动器的版本信息

        :return: The revision of this Drive.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this Drive.

        驱动器的版本信息

        :param revision: The revision of this Drive.
        :type revision: str
        """
        self._revision = revision

    @property
    def media_type(self):
        r"""Gets the media_type of this Drive.

        驱动器的介质类型

        :return: The media_type of this Drive.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        r"""Sets the media_type of this Drive.

        驱动器的介质类型

        :param media_type: The media_type of this Drive.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def protocol(self):
        r"""Gets the protocol of this Drive.

        驱动器遵从的协议

        :return: The protocol of this Drive.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Drive.

        驱动器遵从的协议

        :param protocol: The protocol of this Drive.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def sas_address(self):
        r"""Gets the sas_address of this Drive.

        SAS地址

        :return: The sas_address of this Drive.
        :rtype: str
        """
        return self._sas_address

    @sas_address.setter
    def sas_address(self, sas_address):
        r"""Sets the sas_address of this Drive.

        SAS地址

        :param sas_address: The sas_address of this Drive.
        :type sas_address: str
        """
        self._sas_address = sas_address

    @property
    def capacity_bytes(self):
        r"""Gets the capacity_bytes of this Drive.

        容量（单位：byte）

        :return: The capacity_bytes of this Drive.
        :rtype: int
        """
        return self._capacity_bytes

    @capacity_bytes.setter
    def capacity_bytes(self, capacity_bytes):
        r"""Sets the capacity_bytes of this Drive.

        容量（单位：byte）

        :param capacity_bytes: The capacity_bytes of this Drive.
        :type capacity_bytes: int
        """
        self._capacity_bytes = capacity_bytes

    @property
    def capable_speed_gbs(self):
        r"""Gets the capable_speed_gbs of this Drive.

        驱动器接口的最大速率（单位：Gbps）

        :return: The capable_speed_gbs of this Drive.
        :rtype: int
        """
        return self._capable_speed_gbs

    @capable_speed_gbs.setter
    def capable_speed_gbs(self, capable_speed_gbs):
        r"""Sets the capable_speed_gbs of this Drive.

        驱动器接口的最大速率（单位：Gbps）

        :param capable_speed_gbs: The capable_speed_gbs of this Drive.
        :type capable_speed_gbs: int
        """
        self._capable_speed_gbs = capable_speed_gbs

    @property
    def negotiated_speed_gbs(self):
        r"""Gets the negotiated_speed_gbs of this Drive.

        驱动器接口的协商速率（单位：Gbps）

        :return: The negotiated_speed_gbs of this Drive.
        :rtype: int
        """
        return self._negotiated_speed_gbs

    @negotiated_speed_gbs.setter
    def negotiated_speed_gbs(self, negotiated_speed_gbs):
        r"""Sets the negotiated_speed_gbs of this Drive.

        驱动器接口的协商速率（单位：Gbps）

        :param negotiated_speed_gbs: The negotiated_speed_gbs of this Drive.
        :type negotiated_speed_gbs: int
        """
        self._negotiated_speed_gbs = negotiated_speed_gbs

    @property
    def hotspare_type(self):
        r"""Gets the hotspare_type of this Drive.

        驱动器的热备状态

        :return: The hotspare_type of this Drive.
        :rtype: str
        """
        return self._hotspare_type

    @hotspare_type.setter
    def hotspare_type(self, hotspare_type):
        r"""Sets the hotspare_type of this Drive.

        驱动器的热备状态

        :param hotspare_type: The hotspare_type of this Drive.
        :type hotspare_type: str
        """
        self._hotspare_type = hotspare_type

    @property
    def hours_of_powered_up(self):
        r"""Gets the hours_of_powered_up of this Drive.

        驱动器上电运行时间（单位：h）

        :return: The hours_of_powered_up of this Drive.
        :rtype: int
        """
        return self._hours_of_powered_up

    @hours_of_powered_up.setter
    def hours_of_powered_up(self, hours_of_powered_up):
        r"""Sets the hours_of_powered_up of this Drive.

        驱动器上电运行时间（单位：h）

        :param hours_of_powered_up: The hours_of_powered_up of this Drive.
        :type hours_of_powered_up: int
        """
        self._hours_of_powered_up = hours_of_powered_up

    @property
    def power_state(self):
        r"""Gets the power_state of this Drive.

        驱动器电源状态

        :return: The power_state of this Drive.
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        r"""Sets the power_state of this Drive.

        驱动器电源状态

        :param power_state: The power_state of this Drive.
        :type power_state: str
        """
        self._power_state = power_state

    @property
    def patrol_state(self):
        r"""Gets the patrol_state of this Drive.

        驱动器巡检状态

        :return: The patrol_state of this Drive.
        :rtype: str
        """
        return self._patrol_state

    @patrol_state.setter
    def patrol_state(self, patrol_state):
        r"""Sets the patrol_state of this Drive.

        驱动器巡检状态

        :param patrol_state: The patrol_state of this Drive.
        :type patrol_state: str
        """
        self._patrol_state = patrol_state

    @property
    def associated_resource(self):
        r"""Gets the associated_resource of this Drive.

        驱动器的资源归属

        :return: The associated_resource of this Drive.
        :rtype: str
        """
        return self._associated_resource

    @associated_resource.setter
    def associated_resource(self, associated_resource):
        r"""Sets the associated_resource of this Drive.

        驱动器的资源归属

        :param associated_resource: The associated_resource of this Drive.
        :type associated_resource: str
        """
        self._associated_resource = associated_resource

    @property
    def predicted_media_life_left_percent(self):
        r"""Gets the predicted_media_life_left_percent of this Drive.

        驱动器的剩余寿命百分比

        :return: The predicted_media_life_left_percent of this Drive.
        :rtype: int
        """
        return self._predicted_media_life_left_percent

    @predicted_media_life_left_percent.setter
    def predicted_media_life_left_percent(self, predicted_media_life_left_percent):
        r"""Sets the predicted_media_life_left_percent of this Drive.

        驱动器的剩余寿命百分比

        :param predicted_media_life_left_percent: The predicted_media_life_left_percent of this Drive.
        :type predicted_media_life_left_percent: int
        """
        self._predicted_media_life_left_percent = predicted_media_life_left_percent

    @property
    def health(self):
        r"""Gets the health of this Drive.

        健康状态

        :return: The health of this Drive.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this Drive.

        健康状态

        :param health: The health of this Drive.
        :type health: str
        """
        self._health = health

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
        if not isinstance(other, Drive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
