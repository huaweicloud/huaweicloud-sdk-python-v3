# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecIssueStayTimesResponseBodyData:

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
        'stay_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'stay_time': 'stay_time'
    }

    def __init__(self, id=None, stay_time=None):
        r"""ListSpecIssueStayTimesResponseBodyData

        The model defined in huaweicloud sdk

        :param id: 工作项id字符串
        :type id: str
        :param stay_time: 停留时间（单位：秒）
        :type stay_time: int
        """
        
        

        self._id = None
        self._stay_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if stay_time is not None:
            self.stay_time = stay_time

    @property
    def id(self):
        r"""Gets the id of this ListSpecIssueStayTimesResponseBodyData.

        工作项id字符串

        :return: The id of this ListSpecIssueStayTimesResponseBodyData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSpecIssueStayTimesResponseBodyData.

        工作项id字符串

        :param id: The id of this ListSpecIssueStayTimesResponseBodyData.
        :type id: str
        """
        self._id = id

    @property
    def stay_time(self):
        r"""Gets the stay_time of this ListSpecIssueStayTimesResponseBodyData.

        停留时间（单位：秒）

        :return: The stay_time of this ListSpecIssueStayTimesResponseBodyData.
        :rtype: int
        """
        return self._stay_time

    @stay_time.setter
    def stay_time(self, stay_time):
        r"""Sets the stay_time of this ListSpecIssueStayTimesResponseBodyData.

        停留时间（单位：秒）

        :param stay_time: The stay_time of this ListSpecIssueStayTimesResponseBodyData.
        :type stay_time: int
        """
        self._stay_time = stay_time

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
        if not isinstance(other, ListSpecIssueStayTimesResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
