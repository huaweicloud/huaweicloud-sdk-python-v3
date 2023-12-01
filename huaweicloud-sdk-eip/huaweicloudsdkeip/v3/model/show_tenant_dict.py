# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantDict:

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
        'charge_mode': 'str',
        'min_size': 'int',
        'max_size': 'int',
        'ext_limit': 'ExtLimitPojo'
    }

    attribute_map = {
        'id': 'id',
        'charge_mode': 'charge_mode',
        'min_size': 'min_size',
        'max_size': 'max_size',
        'ext_limit': 'ext_limit'
    }

    def __init__(self, id=None, charge_mode=None, min_size=None, max_size=None, ext_limit=None):
        """ShowTenantDict

        The model defined in huaweicloud sdk

        :param id: - 功能说明：弹性公网IP的唯一标识
        :type id: str
        :param charge_mode: 带宽的计费模式
        :type charge_mode: str
        :param min_size: 该类型带宽可购买的最小size
        :type min_size: int
        :param max_size: 该类型带宽可购买的最大size
        :type max_size: int
        :param ext_limit: 
        :type ext_limit: :class:`huaweicloudsdkeip.v3.ExtLimitPojo`
        """
        
        

        self._id = None
        self._charge_mode = None
        self._min_size = None
        self._max_size = None
        self._ext_limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if ext_limit is not None:
            self.ext_limit = ext_limit

    @property
    def id(self):
        """Gets the id of this ShowTenantDict.

        - 功能说明：弹性公网IP的唯一标识

        :return: The id of this ShowTenantDict.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowTenantDict.

        - 功能说明：弹性公网IP的唯一标识

        :param id: The id of this ShowTenantDict.
        :type id: str
        """
        self._id = id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ShowTenantDict.

        带宽的计费模式

        :return: The charge_mode of this ShowTenantDict.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ShowTenantDict.

        带宽的计费模式

        :param charge_mode: The charge_mode of this ShowTenantDict.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def min_size(self):
        """Gets the min_size of this ShowTenantDict.

        该类型带宽可购买的最小size

        :return: The min_size of this ShowTenantDict.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this ShowTenantDict.

        该类型带宽可购买的最小size

        :param min_size: The min_size of this ShowTenantDict.
        :type min_size: int
        """
        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this ShowTenantDict.

        该类型带宽可购买的最大size

        :return: The max_size of this ShowTenantDict.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this ShowTenantDict.

        该类型带宽可购买的最大size

        :param max_size: The max_size of this ShowTenantDict.
        :type max_size: int
        """
        self._max_size = max_size

    @property
    def ext_limit(self):
        """Gets the ext_limit of this ShowTenantDict.

        :return: The ext_limit of this ShowTenantDict.
        :rtype: :class:`huaweicloudsdkeip.v3.ExtLimitPojo`
        """
        return self._ext_limit

    @ext_limit.setter
    def ext_limit(self, ext_limit):
        """Sets the ext_limit of this ShowTenantDict.

        :param ext_limit: The ext_limit of this ShowTenantDict.
        :type ext_limit: :class:`huaweicloudsdkeip.v3.ExtLimitPojo`
        """
        self._ext_limit = ext_limit

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
        if not isinstance(other, ShowTenantDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
