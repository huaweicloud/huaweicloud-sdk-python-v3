# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitsCommits:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sha': 'str',
        'message': 'str',
        'authored_date': 'str'
    }

    attribute_map = {
        'sha': 'sha',
        'message': 'message',
        'authored_date': 'authored_date'
    }

    def __init__(self, sha=None, message=None, authored_date=None):
        """CommitsCommits

        The model defined in huaweicloud sdk

        :param sha: 提交记录sha值。
        :type sha: str
        :param message: 提交记录描述。
        :type message: str
        :param authored_date: 合入时间。
        :type authored_date: str
        """
        
        

        self._sha = None
        self._message = None
        self._authored_date = None
        self.discriminator = None

        self.sha = sha
        self.message = message
        self.authored_date = authored_date

    @property
    def sha(self):
        """Gets the sha of this CommitsCommits.

        提交记录sha值。

        :return: The sha of this CommitsCommits.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this CommitsCommits.

        提交记录sha值。

        :param sha: The sha of this CommitsCommits.
        :type sha: str
        """
        self._sha = sha

    @property
    def message(self):
        """Gets the message of this CommitsCommits.

        提交记录描述。

        :return: The message of this CommitsCommits.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommitsCommits.

        提交记录描述。

        :param message: The message of this CommitsCommits.
        :type message: str
        """
        self._message = message

    @property
    def authored_date(self):
        """Gets the authored_date of this CommitsCommits.

        合入时间。

        :return: The authored_date of this CommitsCommits.
        :rtype: str
        """
        return self._authored_date

    @authored_date.setter
    def authored_date(self, authored_date):
        """Sets the authored_date of this CommitsCommits.

        合入时间。

        :param authored_date: The authored_date of this CommitsCommits.
        :type authored_date: str
        """
        self._authored_date = authored_date

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
        if not isinstance(other, CommitsCommits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
