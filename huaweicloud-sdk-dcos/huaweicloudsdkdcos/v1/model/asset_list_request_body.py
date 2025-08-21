# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_sn_list': 'list[str]',
        'asset_type': 'list[str]',
        'start_first_inbound_time': 'str',
        'end_first_inbound_time': 'str',
        'model': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'asset_sn_list': 'asset_sn_list',
        'asset_type': 'asset_type',
        'start_first_inbound_time': 'start_first_inbound_time',
        'end_first_inbound_time': 'end_first_inbound_time',
        'model': 'model',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, asset_sn_list=None, asset_type=None, start_first_inbound_time=None, end_first_inbound_time=None, model=None, name=None, offset=None, limit=None):
        r"""AssetListRequestBody

        The model defined in huaweicloud sdk

        :param asset_sn_list: 资产序列号
        :type asset_sn_list: list[str]
        :param asset_type: 资产大类
        :type asset_type: list[str]
        :param start_first_inbound_time: 首次入库时间搜索起始时间
        :type start_first_inbound_time: str
        :param end_first_inbound_time: 首次入库时间搜索结束时间
        :type end_first_inbound_time: str
        :param model: 资产模型
        :type model: str
        :param name: 资产名称
        :type name: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页条目数量
        :type limit: int
        """
        
        

        self._asset_sn_list = None
        self._asset_type = None
        self._start_first_inbound_time = None
        self._end_first_inbound_time = None
        self._model = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if asset_sn_list is not None:
            self.asset_sn_list = asset_sn_list
        if asset_type is not None:
            self.asset_type = asset_type
        if start_first_inbound_time is not None:
            self.start_first_inbound_time = start_first_inbound_time
        if end_first_inbound_time is not None:
            self.end_first_inbound_time = end_first_inbound_time
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        self.offset = offset
        self.limit = limit

    @property
    def asset_sn_list(self):
        r"""Gets the asset_sn_list of this AssetListRequestBody.

        资产序列号

        :return: The asset_sn_list of this AssetListRequestBody.
        :rtype: list[str]
        """
        return self._asset_sn_list

    @asset_sn_list.setter
    def asset_sn_list(self, asset_sn_list):
        r"""Sets the asset_sn_list of this AssetListRequestBody.

        资产序列号

        :param asset_sn_list: The asset_sn_list of this AssetListRequestBody.
        :type asset_sn_list: list[str]
        """
        self._asset_sn_list = asset_sn_list

    @property
    def asset_type(self):
        r"""Gets the asset_type of this AssetListRequestBody.

        资产大类

        :return: The asset_type of this AssetListRequestBody.
        :rtype: list[str]
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this AssetListRequestBody.

        资产大类

        :param asset_type: The asset_type of this AssetListRequestBody.
        :type asset_type: list[str]
        """
        self._asset_type = asset_type

    @property
    def start_first_inbound_time(self):
        r"""Gets the start_first_inbound_time of this AssetListRequestBody.

        首次入库时间搜索起始时间

        :return: The start_first_inbound_time of this AssetListRequestBody.
        :rtype: str
        """
        return self._start_first_inbound_time

    @start_first_inbound_time.setter
    def start_first_inbound_time(self, start_first_inbound_time):
        r"""Sets the start_first_inbound_time of this AssetListRequestBody.

        首次入库时间搜索起始时间

        :param start_first_inbound_time: The start_first_inbound_time of this AssetListRequestBody.
        :type start_first_inbound_time: str
        """
        self._start_first_inbound_time = start_first_inbound_time

    @property
    def end_first_inbound_time(self):
        r"""Gets the end_first_inbound_time of this AssetListRequestBody.

        首次入库时间搜索结束时间

        :return: The end_first_inbound_time of this AssetListRequestBody.
        :rtype: str
        """
        return self._end_first_inbound_time

    @end_first_inbound_time.setter
    def end_first_inbound_time(self, end_first_inbound_time):
        r"""Sets the end_first_inbound_time of this AssetListRequestBody.

        首次入库时间搜索结束时间

        :param end_first_inbound_time: The end_first_inbound_time of this AssetListRequestBody.
        :type end_first_inbound_time: str
        """
        self._end_first_inbound_time = end_first_inbound_time

    @property
    def model(self):
        r"""Gets the model of this AssetListRequestBody.

        资产模型

        :return: The model of this AssetListRequestBody.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this AssetListRequestBody.

        资产模型

        :param model: The model of this AssetListRequestBody.
        :type model: str
        """
        self._model = model

    @property
    def name(self):
        r"""Gets the name of this AssetListRequestBody.

        资产名称

        :return: The name of this AssetListRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetListRequestBody.

        资产名称

        :param name: The name of this AssetListRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this AssetListRequestBody.

        偏移量

        :return: The offset of this AssetListRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this AssetListRequestBody.

        偏移量

        :param offset: The offset of this AssetListRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this AssetListRequestBody.

        每页条目数量

        :return: The limit of this AssetListRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this AssetListRequestBody.

        每页条目数量

        :param limit: The limit of this AssetListRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, AssetListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
