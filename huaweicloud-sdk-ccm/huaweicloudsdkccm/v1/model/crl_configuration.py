# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CrlConfiguration:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'crl_dis_point': 'str',
        'crl_name': 'str',
        'enabled': 'bool',
        'obs_bucket_name': 'str',
        'valid_days': 'int'
    }

    attribute_map = {
        'crl_dis_point': 'crl_dis_point',
        'crl_name': 'crl_name',
        'enabled': 'enabled',
        'obs_bucket_name': 'obs_bucket_name',
        'valid_days': 'valid_days'
    }

    def __init__(self, crl_dis_point=None, crl_name=None, enabled=None, obs_bucket_name=None, valid_days=None):
        """CrlConfiguration - a model defined in huaweicloud sdk"""
        
        

        self._crl_dis_point = None
        self._crl_name = None
        self._enabled = None
        self._obs_bucket_name = None
        self._valid_days = None
        self.discriminator = None

        if crl_dis_point is not None:
            self.crl_dis_point = crl_dis_point
        if crl_name is not None:
            self.crl_name = crl_name
        if enabled is not None:
            self.enabled = enabled
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if valid_days is not None:
            self.valid_days = valid_days

    @property
    def crl_dis_point(self):
        """Gets the crl_dis_point of this CrlConfiguration.

        吊销列表分发地址

        :return: The crl_dis_point of this CrlConfiguration.
        :rtype: str
        """
        return self._crl_dis_point

    @crl_dis_point.setter
    def crl_dis_point(self, crl_dis_point):
        """Sets the crl_dis_point of this CrlConfiguration.

        吊销列表分发地址

        :param crl_dis_point: The crl_dis_point of this CrlConfiguration.
        :type: str
        """
        self._crl_dis_point = crl_dis_point

    @property
    def crl_name(self):
        """Gets the crl_name of this CrlConfiguration.

        吊销列表文件名称

        :return: The crl_name of this CrlConfiguration.
        :rtype: str
        """
        return self._crl_name

    @crl_name.setter
    def crl_name(self, crl_name):
        """Sets the crl_name of this CrlConfiguration.

        吊销列表文件名称

        :param crl_name: The crl_name of this CrlConfiguration.
        :type: str
        """
        self._crl_name = crl_name

    @property
    def enabled(self):
        """Gets the enabled of this CrlConfiguration.

        是否启用CRL发布功能

        :return: The enabled of this CrlConfiguration.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CrlConfiguration.

        是否启用CRL发布功能

        :param enabled: The enabled of this CrlConfiguration.
        :type: bool
        """
        self._enabled = enabled

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this CrlConfiguration.

        OBS桶名称

        :return: The obs_bucket_name of this CrlConfiguration.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this CrlConfiguration.

        OBS桶名称

        :param obs_bucket_name: The obs_bucket_name of this CrlConfiguration.
        :type: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def valid_days(self):
        """Gets the valid_days of this CrlConfiguration.

        更新周期

        :return: The valid_days of this CrlConfiguration.
        :rtype: int
        """
        return self._valid_days

    @valid_days.setter
    def valid_days(self, valid_days):
        """Sets the valid_days of this CrlConfiguration.

        更新周期

        :param valid_days: The valid_days of this CrlConfiguration.
        :type: int
        """
        self._valid_days = valid_days

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
        if not isinstance(other, CrlConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
