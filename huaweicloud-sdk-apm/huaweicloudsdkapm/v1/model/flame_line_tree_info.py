# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlameLineTreeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'to': 'int',
        'type': 'str',
        'instance_id': 'int',
        'api': 'str',
        'region': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'type': 'type',
        'instance_id': 'instance_id',
        'api': 'api',
        'region': 'region'
    }

    def __init__(self, _from=None, to=None, type=None, instance_id=None, api=None, region=None):
        r"""FlameLineTreeInfo

        The model defined in huaweicloud sdk

        :param _from: 开始时间，比如1704271204595
        :type _from: int
        :param to: 结束时间, 比如1704275169491
        :type to: int
        :param type: 数据类型, CPU 或者 LATENCY
        :type type: str
        :param instance_id: 实例id
        :type instance_id: int
        :param api: api的url,比如: GET_/user/{id}
        :type api: str
        :param region: 实例所在区域
        :type region: str
        """
        
        

        self.__from = None
        self._to = None
        self._type = None
        self._instance_id = None
        self._api = None
        self._region = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.type = type
        self.instance_id = instance_id
        self.api = api
        self.region = region

    @property
    def _from(self):
        r"""Gets the _from of this FlameLineTreeInfo.

        开始时间，比如1704271204595

        :return: The _from of this FlameLineTreeInfo.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this FlameLineTreeInfo.

        开始时间，比如1704271204595

        :param _from: The _from of this FlameLineTreeInfo.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this FlameLineTreeInfo.

        结束时间, 比如1704275169491

        :return: The to of this FlameLineTreeInfo.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this FlameLineTreeInfo.

        结束时间, 比如1704275169491

        :param to: The to of this FlameLineTreeInfo.
        :type to: int
        """
        self._to = to

    @property
    def type(self):
        r"""Gets the type of this FlameLineTreeInfo.

        数据类型, CPU 或者 LATENCY

        :return: The type of this FlameLineTreeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlameLineTreeInfo.

        数据类型, CPU 或者 LATENCY

        :param type: The type of this FlameLineTreeInfo.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this FlameLineTreeInfo.

        实例id

        :return: The instance_id of this FlameLineTreeInfo.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this FlameLineTreeInfo.

        实例id

        :param instance_id: The instance_id of this FlameLineTreeInfo.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def api(self):
        r"""Gets the api of this FlameLineTreeInfo.

        api的url,比如: GET_/user/{id}

        :return: The api of this FlameLineTreeInfo.
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        r"""Sets the api of this FlameLineTreeInfo.

        api的url,比如: GET_/user/{id}

        :param api: The api of this FlameLineTreeInfo.
        :type api: str
        """
        self._api = api

    @property
    def region(self):
        r"""Gets the region of this FlameLineTreeInfo.

        实例所在区域

        :return: The region of this FlameLineTreeInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this FlameLineTreeInfo.

        实例所在区域

        :param region: The region of this FlameLineTreeInfo.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, FlameLineTreeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
