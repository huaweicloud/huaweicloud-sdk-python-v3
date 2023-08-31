# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'rolling_release': 'DeployStrategyRollingRelease',
        'gray_release': 'DeployStrategyGrayRelease'
    }

    attribute_map = {
        'type': 'type',
        'rolling_release': 'rolling_release',
        'gray_release': 'gray_release'
    }

    def __init__(self, type=None, rolling_release=None, gray_release=None):
        """DeployStrategy

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param rolling_release: 
        :type rolling_release: :class:`huaweicloudsdkservicestage.v3.DeployStrategyRollingRelease`
        :param gray_release: 
        :type gray_release: :class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayRelease`
        """
        
        

        self._type = None
        self._rolling_release = None
        self._gray_release = None
        self.discriminator = None

        self.type = type
        if rolling_release is not None:
            self.rolling_release = rolling_release
        if gray_release is not None:
            self.gray_release = gray_release

    @property
    def type(self):
        """Gets the type of this DeployStrategy.

        :return: The type of this DeployStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeployStrategy.

        :param type: The type of this DeployStrategy.
        :type type: str
        """
        self._type = type

    @property
    def rolling_release(self):
        """Gets the rolling_release of this DeployStrategy.

        :return: The rolling_release of this DeployStrategy.
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeployStrategyRollingRelease`
        """
        return self._rolling_release

    @rolling_release.setter
    def rolling_release(self, rolling_release):
        """Sets the rolling_release of this DeployStrategy.

        :param rolling_release: The rolling_release of this DeployStrategy.
        :type rolling_release: :class:`huaweicloudsdkservicestage.v3.DeployStrategyRollingRelease`
        """
        self._rolling_release = rolling_release

    @property
    def gray_release(self):
        """Gets the gray_release of this DeployStrategy.

        :return: The gray_release of this DeployStrategy.
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayRelease`
        """
        return self._gray_release

    @gray_release.setter
    def gray_release(self, gray_release):
        """Sets the gray_release of this DeployStrategy.

        :param gray_release: The gray_release of this DeployStrategy.
        :type gray_release: :class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayRelease`
        """
        self._gray_release = gray_release

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
        if not isinstance(other, DeployStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
