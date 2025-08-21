# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Asset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_sn': 'str',
        'name': 'str',
        'model': 'str',
        'asset_type': 'str',
        'max_type_cn_name': 'str',
        'max_type_en_name': 'str',
        'asset_status': 'str',
        'dc_name': 'str',
        'dc_code': 'str',
        'room_name': 'str',
        'room_code': 'str',
        'rack_id': 'str',
        'first_inbound_time': 'str',
        'outbound_time': 'str',
        'inbound_time': 'str',
        'mount_sn': 'str'
    }

    attribute_map = {
        'asset_sn': 'asset_sn',
        'name': 'name',
        'model': 'model',
        'asset_type': 'asset_type',
        'max_type_cn_name': 'max_type_cn_name',
        'max_type_en_name': 'max_type_en_name',
        'asset_status': 'asset_status',
        'dc_name': 'dc_name',
        'dc_code': 'dc_code',
        'room_name': 'room_name',
        'room_code': 'room_code',
        'rack_id': 'rack_id',
        'first_inbound_time': 'first_inbound_time',
        'outbound_time': 'outbound_time',
        'inbound_time': 'inbound_time',
        'mount_sn': 'mount_sn'
    }

    def __init__(self, asset_sn=None, name=None, model=None, asset_type=None, max_type_cn_name=None, max_type_en_name=None, asset_status=None, dc_name=None, dc_code=None, room_name=None, room_code=None, rack_id=None, first_inbound_time=None, outbound_time=None, inbound_time=None, mount_sn=None):
        r"""Asset

        The model defined in huaweicloud sdk

        :param asset_sn: 资产sn
        :type asset_sn: str
        :param name: 资产名称
        :type name: str
        :param model: 资产类型
        :type model: str
        :param asset_type: 资产大类
        :type asset_type: str
        :param max_type_cn_name: 资产大类-中文
        :type max_type_cn_name: str
        :param max_type_en_name: 资产大类-英文
        :type max_type_en_name: str
        :param asset_status: 资产状态
        :type asset_status: str
        :param dc_name: dc名称
        :type dc_name: str
        :param dc_code: dc编码
        :type dc_code: str
        :param room_name: 房间名称
        :type room_name: str
        :param room_code: 机房编码
        :type room_code: str
        :param rack_id: 机柜编码
        :type rack_id: str
        :param first_inbound_time: 首次入库时间
        :type first_inbound_time: str
        :param outbound_time: 出库时间
        :type outbound_time: str
        :param inbound_time: 入库时间
        :type inbound_time: str
        :param mount_sn: 支架sn
        :type mount_sn: str
        """
        
        

        self._asset_sn = None
        self._name = None
        self._model = None
        self._asset_type = None
        self._max_type_cn_name = None
        self._max_type_en_name = None
        self._asset_status = None
        self._dc_name = None
        self._dc_code = None
        self._room_name = None
        self._room_code = None
        self._rack_id = None
        self._first_inbound_time = None
        self._outbound_time = None
        self._inbound_time = None
        self._mount_sn = None
        self.discriminator = None

        if asset_sn is not None:
            self.asset_sn = asset_sn
        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if asset_type is not None:
            self.asset_type = asset_type
        if max_type_cn_name is not None:
            self.max_type_cn_name = max_type_cn_name
        if max_type_en_name is not None:
            self.max_type_en_name = max_type_en_name
        if asset_status is not None:
            self.asset_status = asset_status
        if dc_name is not None:
            self.dc_name = dc_name
        if dc_code is not None:
            self.dc_code = dc_code
        if room_name is not None:
            self.room_name = room_name
        if room_code is not None:
            self.room_code = room_code
        if rack_id is not None:
            self.rack_id = rack_id
        if first_inbound_time is not None:
            self.first_inbound_time = first_inbound_time
        if outbound_time is not None:
            self.outbound_time = outbound_time
        if inbound_time is not None:
            self.inbound_time = inbound_time
        if mount_sn is not None:
            self.mount_sn = mount_sn

    @property
    def asset_sn(self):
        r"""Gets the asset_sn of this Asset.

        资产sn

        :return: The asset_sn of this Asset.
        :rtype: str
        """
        return self._asset_sn

    @asset_sn.setter
    def asset_sn(self, asset_sn):
        r"""Sets the asset_sn of this Asset.

        资产sn

        :param asset_sn: The asset_sn of this Asset.
        :type asset_sn: str
        """
        self._asset_sn = asset_sn

    @property
    def name(self):
        r"""Gets the name of this Asset.

        资产名称

        :return: The name of this Asset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Asset.

        资产名称

        :param name: The name of this Asset.
        :type name: str
        """
        self._name = name

    @property
    def model(self):
        r"""Gets the model of this Asset.

        资产类型

        :return: The model of this Asset.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this Asset.

        资产类型

        :param model: The model of this Asset.
        :type model: str
        """
        self._model = model

    @property
    def asset_type(self):
        r"""Gets the asset_type of this Asset.

        资产大类

        :return: The asset_type of this Asset.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this Asset.

        资产大类

        :param asset_type: The asset_type of this Asset.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def max_type_cn_name(self):
        r"""Gets the max_type_cn_name of this Asset.

        资产大类-中文

        :return: The max_type_cn_name of this Asset.
        :rtype: str
        """
        return self._max_type_cn_name

    @max_type_cn_name.setter
    def max_type_cn_name(self, max_type_cn_name):
        r"""Sets the max_type_cn_name of this Asset.

        资产大类-中文

        :param max_type_cn_name: The max_type_cn_name of this Asset.
        :type max_type_cn_name: str
        """
        self._max_type_cn_name = max_type_cn_name

    @property
    def max_type_en_name(self):
        r"""Gets the max_type_en_name of this Asset.

        资产大类-英文

        :return: The max_type_en_name of this Asset.
        :rtype: str
        """
        return self._max_type_en_name

    @max_type_en_name.setter
    def max_type_en_name(self, max_type_en_name):
        r"""Sets the max_type_en_name of this Asset.

        资产大类-英文

        :param max_type_en_name: The max_type_en_name of this Asset.
        :type max_type_en_name: str
        """
        self._max_type_en_name = max_type_en_name

    @property
    def asset_status(self):
        r"""Gets the asset_status of this Asset.

        资产状态

        :return: The asset_status of this Asset.
        :rtype: str
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        r"""Sets the asset_status of this Asset.

        资产状态

        :param asset_status: The asset_status of this Asset.
        :type asset_status: str
        """
        self._asset_status = asset_status

    @property
    def dc_name(self):
        r"""Gets the dc_name of this Asset.

        dc名称

        :return: The dc_name of this Asset.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        r"""Sets the dc_name of this Asset.

        dc名称

        :param dc_name: The dc_name of this Asset.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def dc_code(self):
        r"""Gets the dc_code of this Asset.

        dc编码

        :return: The dc_code of this Asset.
        :rtype: str
        """
        return self._dc_code

    @dc_code.setter
    def dc_code(self, dc_code):
        r"""Sets the dc_code of this Asset.

        dc编码

        :param dc_code: The dc_code of this Asset.
        :type dc_code: str
        """
        self._dc_code = dc_code

    @property
    def room_name(self):
        r"""Gets the room_name of this Asset.

        房间名称

        :return: The room_name of this Asset.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this Asset.

        房间名称

        :param room_name: The room_name of this Asset.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_code(self):
        r"""Gets the room_code of this Asset.

        机房编码

        :return: The room_code of this Asset.
        :rtype: str
        """
        return self._room_code

    @room_code.setter
    def room_code(self, room_code):
        r"""Sets the room_code of this Asset.

        机房编码

        :param room_code: The room_code of this Asset.
        :type room_code: str
        """
        self._room_code = room_code

    @property
    def rack_id(self):
        r"""Gets the rack_id of this Asset.

        机柜编码

        :return: The rack_id of this Asset.
        :rtype: str
        """
        return self._rack_id

    @rack_id.setter
    def rack_id(self, rack_id):
        r"""Sets the rack_id of this Asset.

        机柜编码

        :param rack_id: The rack_id of this Asset.
        :type rack_id: str
        """
        self._rack_id = rack_id

    @property
    def first_inbound_time(self):
        r"""Gets the first_inbound_time of this Asset.

        首次入库时间

        :return: The first_inbound_time of this Asset.
        :rtype: str
        """
        return self._first_inbound_time

    @first_inbound_time.setter
    def first_inbound_time(self, first_inbound_time):
        r"""Sets the first_inbound_time of this Asset.

        首次入库时间

        :param first_inbound_time: The first_inbound_time of this Asset.
        :type first_inbound_time: str
        """
        self._first_inbound_time = first_inbound_time

    @property
    def outbound_time(self):
        r"""Gets the outbound_time of this Asset.

        出库时间

        :return: The outbound_time of this Asset.
        :rtype: str
        """
        return self._outbound_time

    @outbound_time.setter
    def outbound_time(self, outbound_time):
        r"""Sets the outbound_time of this Asset.

        出库时间

        :param outbound_time: The outbound_time of this Asset.
        :type outbound_time: str
        """
        self._outbound_time = outbound_time

    @property
    def inbound_time(self):
        r"""Gets the inbound_time of this Asset.

        入库时间

        :return: The inbound_time of this Asset.
        :rtype: str
        """
        return self._inbound_time

    @inbound_time.setter
    def inbound_time(self, inbound_time):
        r"""Sets the inbound_time of this Asset.

        入库时间

        :param inbound_time: The inbound_time of this Asset.
        :type inbound_time: str
        """
        self._inbound_time = inbound_time

    @property
    def mount_sn(self):
        r"""Gets the mount_sn of this Asset.

        支架sn

        :return: The mount_sn of this Asset.
        :rtype: str
        """
        return self._mount_sn

    @mount_sn.setter
    def mount_sn(self, mount_sn):
        r"""Sets the mount_sn of this Asset.

        支架sn

        :param mount_sn: The mount_sn of this Asset.
        :type mount_sn: str
        """
        self._mount_sn = mount_sn

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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
