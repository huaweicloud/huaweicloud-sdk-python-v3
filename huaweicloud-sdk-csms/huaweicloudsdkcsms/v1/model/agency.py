# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Agency:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'agency_id': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'agency_id': 'agency_id',
        'error_msg': 'error_msg'
    }

    def __init__(self, agency_name=None, agency_id=None, error_msg=None):
        r"""Agency

        The model defined in huaweicloud sdk

        :param agency_name: 委托名称。
        :type agency_name: str
        :param agency_id: 委托ID。
        :type agency_id: str
        :param error_msg: 异常信息。当委托创建失败时，返回的异常信息。
        :type error_msg: str
        """
        
        

        self._agency_name = None
        self._agency_id = None
        self._error_msg = None
        self.discriminator = None

        self.agency_name = agency_name
        if agency_id is not None:
            self.agency_id = agency_id
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def agency_name(self):
        r"""Gets the agency_name of this Agency.

        委托名称。

        :return: The agency_name of this Agency.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this Agency.

        委托名称。

        :param agency_name: The agency_name of this Agency.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def agency_id(self):
        r"""Gets the agency_id of this Agency.

        委托ID。

        :return: The agency_id of this Agency.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this Agency.

        委托ID。

        :param agency_id: The agency_id of this Agency.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def error_msg(self):
        r"""Gets the error_msg of this Agency.

        异常信息。当委托创建失败时，返回的异常信息。

        :return: The error_msg of this Agency.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this Agency.

        异常信息。当委托创建失败时，返回的异常信息。

        :param error_msg: The error_msg of this Agency.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, Agency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
