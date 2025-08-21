# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'message': 'str',
        'target': 'str',
        'commit': 'CommitDto',
        'x_total': 'str'
    }

    attribute_map = {
        'name': 'name',
        'message': 'message',
        'target': 'target',
        'commit': 'commit',
        'x_total': 'X-Total'
    }

    def __init__(self, name=None, message=None, target=None, commit=None, x_total=None):
        r"""ShowTagResponse

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param message: 标签描述
        :type message: str
        :param target: 基于commitid
        :type target: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowTagResponse, self).__init__()

        self._name = None
        self._message = None
        self._target = None
        self._commit = None
        self._x_total = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if target is not None:
            self.target = target
        if commit is not None:
            self.commit = commit
        if x_total is not None:
            self.x_total = x_total

    @property
    def name(self):
        r"""Gets the name of this ShowTagResponse.

        标签名称

        :return: The name of this ShowTagResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowTagResponse.

        标签名称

        :param name: The name of this ShowTagResponse.
        :type name: str
        """
        self._name = name

    @property
    def message(self):
        r"""Gets the message of this ShowTagResponse.

        标签描述

        :return: The message of this ShowTagResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTagResponse.

        标签描述

        :param message: The message of this ShowTagResponse.
        :type message: str
        """
        self._message = message

    @property
    def target(self):
        r"""Gets the target of this ShowTagResponse.

        基于commitid

        :return: The target of this ShowTagResponse.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ShowTagResponse.

        基于commitid

        :param target: The target of this ShowTagResponse.
        :type target: str
        """
        self._target = target

    @property
    def commit(self):
        r"""Gets the commit of this ShowTagResponse.

        :return: The commit of this ShowTagResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this ShowTagResponse.

        :param commit: The commit of this ShowTagResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        self._commit = commit

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowTagResponse.

        :return: The x_total of this ShowTagResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowTagResponse.

        :param x_total: The x_total of this ShowTagResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
