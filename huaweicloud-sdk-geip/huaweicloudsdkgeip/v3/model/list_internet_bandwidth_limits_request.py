# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidthLimitsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[str]',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'charge_mode': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'charge_mode': 'charge_mode',
        'type': 'type'
    }

    def __init__(self, fields=None, sort_key=None, sort_dir=None, charge_mode=None, type=None):
        """ListInternetBandwidthLimitsRequest

        The model defined in huaweicloud sdk

        :param fields: 
        :type fields: list[str]
        :param sort_key: 按照sort_key指定的字段排序
        :type sort_key: list[str]
        :param sort_dir: 排序的方向，倒序或者正序
        :type sort_dir: list[str]
        :param charge_mode: 
        :type charge_mode: list[str]
        :param type: 
        :type type: str
        """
        
        

        self._fields = None
        self._sort_key = None
        self._sort_dir = None
        self._charge_mode = None
        self._type = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if type is not None:
            self.type = type

    @property
    def fields(self):
        """Gets the fields of this ListInternetBandwidthLimitsRequest.

        :return: The fields of this ListInternetBandwidthLimitsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListInternetBandwidthLimitsRequest.

        :param fields: The fields of this ListInternetBandwidthLimitsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListInternetBandwidthLimitsRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListInternetBandwidthLimitsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListInternetBandwidthLimitsRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListInternetBandwidthLimitsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListInternetBandwidthLimitsRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListInternetBandwidthLimitsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListInternetBandwidthLimitsRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListInternetBandwidthLimitsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListInternetBandwidthLimitsRequest.

        :return: The charge_mode of this ListInternetBandwidthLimitsRequest.
        :rtype: list[str]
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListInternetBandwidthLimitsRequest.

        :param charge_mode: The charge_mode of this ListInternetBandwidthLimitsRequest.
        :type charge_mode: list[str]
        """
        self._charge_mode = charge_mode

    @property
    def type(self):
        """Gets the type of this ListInternetBandwidthLimitsRequest.

        :return: The type of this ListInternetBandwidthLimitsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInternetBandwidthLimitsRequest.

        :param type: The type of this ListInternetBandwidthLimitsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListInternetBandwidthLimitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
