# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomConnectorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'res_code': 'int',
        'res_log': 'str',
        'res_msg': 'str'
    }

    attribute_map = {
        'res_code': 'res_code',
        'res_log': 'res_log',
        'res_msg': 'res_msg'
    }

    def __init__(self, res_code=None, res_log=None, res_msg=None):
        """ShowCustomConnectorResponse

        The model defined in huaweicloud sdk

        :param res_code: 状态码
        :type res_code: int
        :param res_log: 成功信息
        :type res_log: str
        :param res_msg: 成功信息
        :type res_msg: str
        """
        
        super(ShowCustomConnectorResponse, self).__init__()

        self._res_code = None
        self._res_log = None
        self._res_msg = None
        self.discriminator = None

        if res_code is not None:
            self.res_code = res_code
        if res_log is not None:
            self.res_log = res_log
        if res_msg is not None:
            self.res_msg = res_msg

    @property
    def res_code(self):
        """Gets the res_code of this ShowCustomConnectorResponse.

        状态码

        :return: The res_code of this ShowCustomConnectorResponse.
        :rtype: int
        """
        return self._res_code

    @res_code.setter
    def res_code(self, res_code):
        """Sets the res_code of this ShowCustomConnectorResponse.

        状态码

        :param res_code: The res_code of this ShowCustomConnectorResponse.
        :type res_code: int
        """
        self._res_code = res_code

    @property
    def res_log(self):
        """Gets the res_log of this ShowCustomConnectorResponse.

        成功信息

        :return: The res_log of this ShowCustomConnectorResponse.
        :rtype: str
        """
        return self._res_log

    @res_log.setter
    def res_log(self, res_log):
        """Sets the res_log of this ShowCustomConnectorResponse.

        成功信息

        :param res_log: The res_log of this ShowCustomConnectorResponse.
        :type res_log: str
        """
        self._res_log = res_log

    @property
    def res_msg(self):
        """Gets the res_msg of this ShowCustomConnectorResponse.

        成功信息

        :return: The res_msg of this ShowCustomConnectorResponse.
        :rtype: str
        """
        return self._res_msg

    @res_msg.setter
    def res_msg(self, res_msg):
        """Sets the res_msg of this ShowCustomConnectorResponse.

        成功信息

        :param res_msg: The res_msg of this ShowCustomConnectorResponse.
        :type res_msg: str
        """
        self._res_msg = res_msg

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
        if not isinstance(other, ShowCustomConnectorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
