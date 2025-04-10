# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckCallNumberInConfResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'in_conf': 'bool',
        'conf_id': 'str'
    }

    attribute_map = {
        'in_conf': 'in_conf',
        'conf_id': 'conf_id'
    }

    def __init__(self, in_conf=None, conf_id=None):
        r"""CheckCallNumberInConfResponse

        The model defined in huaweicloud sdk

        :param in_conf: 是否在会议中
        :type in_conf: bool
        :param conf_id: 会议id
        :type conf_id: str
        """
        
        super(CheckCallNumberInConfResponse, self).__init__()

        self._in_conf = None
        self._conf_id = None
        self.discriminator = None

        if in_conf is not None:
            self.in_conf = in_conf
        if conf_id is not None:
            self.conf_id = conf_id

    @property
    def in_conf(self):
        r"""Gets the in_conf of this CheckCallNumberInConfResponse.

        是否在会议中

        :return: The in_conf of this CheckCallNumberInConfResponse.
        :rtype: bool
        """
        return self._in_conf

    @in_conf.setter
    def in_conf(self, in_conf):
        r"""Sets the in_conf of this CheckCallNumberInConfResponse.

        是否在会议中

        :param in_conf: The in_conf of this CheckCallNumberInConfResponse.
        :type in_conf: bool
        """
        self._in_conf = in_conf

    @property
    def conf_id(self):
        r"""Gets the conf_id of this CheckCallNumberInConfResponse.

        会议id

        :return: The conf_id of this CheckCallNumberInConfResponse.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        r"""Sets the conf_id of this CheckCallNumberInConfResponse.

        会议id

        :param conf_id: The conf_id of this CheckCallNumberInConfResponse.
        :type conf_id: str
        """
        self._conf_id = conf_id

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
        if not isinstance(other, CheckCallNumberInConfResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
