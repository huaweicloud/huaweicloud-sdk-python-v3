# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMultiCloudClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_expiration_date': 'int',
        'upgrade': 'bool',
        'kubeconfig': 'str'
    }

    attribute_map = {
        'current_expiration_date': 'current_expiration_date',
        'upgrade': 'upgrade',
        'kubeconfig': 'kubeconfig'
    }

    def __init__(self, current_expiration_date=None, upgrade=None, kubeconfig=None):
        r"""UpdateMultiCloudClusterRequestBody

        The model defined in huaweicloud sdk

        :param current_expiration_date: 当前有效期结束时间
        :type current_expiration_date: int
        :param upgrade: 是否升级代理版本
        :type upgrade: bool
        :param kubeconfig: kubeconfig文件
        :type kubeconfig: str
        """
        
        

        self._current_expiration_date = None
        self._upgrade = None
        self._kubeconfig = None
        self.discriminator = None

        self.current_expiration_date = current_expiration_date
        if upgrade is not None:
            self.upgrade = upgrade
        if kubeconfig is not None:
            self.kubeconfig = kubeconfig

    @property
    def current_expiration_date(self):
        r"""Gets the current_expiration_date of this UpdateMultiCloudClusterRequestBody.

        当前有效期结束时间

        :return: The current_expiration_date of this UpdateMultiCloudClusterRequestBody.
        :rtype: int
        """
        return self._current_expiration_date

    @current_expiration_date.setter
    def current_expiration_date(self, current_expiration_date):
        r"""Sets the current_expiration_date of this UpdateMultiCloudClusterRequestBody.

        当前有效期结束时间

        :param current_expiration_date: The current_expiration_date of this UpdateMultiCloudClusterRequestBody.
        :type current_expiration_date: int
        """
        self._current_expiration_date = current_expiration_date

    @property
    def upgrade(self):
        r"""Gets the upgrade of this UpdateMultiCloudClusterRequestBody.

        是否升级代理版本

        :return: The upgrade of this UpdateMultiCloudClusterRequestBody.
        :rtype: bool
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        r"""Sets the upgrade of this UpdateMultiCloudClusterRequestBody.

        是否升级代理版本

        :param upgrade: The upgrade of this UpdateMultiCloudClusterRequestBody.
        :type upgrade: bool
        """
        self._upgrade = upgrade

    @property
    def kubeconfig(self):
        r"""Gets the kubeconfig of this UpdateMultiCloudClusterRequestBody.

        kubeconfig文件

        :return: The kubeconfig of this UpdateMultiCloudClusterRequestBody.
        :rtype: str
        """
        return self._kubeconfig

    @kubeconfig.setter
    def kubeconfig(self, kubeconfig):
        r"""Sets the kubeconfig of this UpdateMultiCloudClusterRequestBody.

        kubeconfig文件

        :param kubeconfig: The kubeconfig of this UpdateMultiCloudClusterRequestBody.
        :type kubeconfig: str
        """
        self._kubeconfig = kubeconfig

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
        if not isinstance(other, UpdateMultiCloudClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
