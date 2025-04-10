# coding: utf-8

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
        'enabled': 'bool',
        'crl_name': 'str',
        'obs_bucket_name': 'str',
        'valid_days': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'crl_name': 'crl_name',
        'obs_bucket_name': 'obs_bucket_name',
        'valid_days': 'valid_days'
    }

    def __init__(self, enabled=None, crl_name=None, obs_bucket_name=None, valid_days=None):
        r"""CrlConfiguration

        The model defined in huaweicloud sdk

        :param enabled: 是否启用CRL发布功能。 - **true** - **false**
        :type enabled: bool
        :param crl_name: 吊销列表文件名称。 &gt; 若用户不指定，系统将默认采用当前证书的父CA ID。
        :type crl_name: str
        :param obs_bucket_name: OBS桶名称。 &gt; 当需要启用CRL发布功能： &gt; - 此参数为必填项，且用户必须已创建委托授权，授予PCA服务对OBS的相关权限，具体参见本文档：**证书吊销处理&gt;查看是否具有委托权限**、**证书吊销处理&gt;创建委托**； &gt; - 指定的OBS桶必须存在，否则将报错。
        :type obs_bucket_name: str
        :param valid_days: CRL更新周期，单位为\&quot;天\&quot;。当启用CRL发布功能，为必填项。
        :type valid_days: int
        """
        
        

        self._enabled = None
        self._crl_name = None
        self._obs_bucket_name = None
        self._valid_days = None
        self.discriminator = None

        self.enabled = enabled
        if crl_name is not None:
            self.crl_name = crl_name
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if valid_days is not None:
            self.valid_days = valid_days

    @property
    def enabled(self):
        r"""Gets the enabled of this CrlConfiguration.

        是否启用CRL发布功能。 - **true** - **false**

        :return: The enabled of this CrlConfiguration.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CrlConfiguration.

        是否启用CRL发布功能。 - **true** - **false**

        :param enabled: The enabled of this CrlConfiguration.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def crl_name(self):
        r"""Gets the crl_name of this CrlConfiguration.

        吊销列表文件名称。 > 若用户不指定，系统将默认采用当前证书的父CA ID。

        :return: The crl_name of this CrlConfiguration.
        :rtype: str
        """
        return self._crl_name

    @crl_name.setter
    def crl_name(self, crl_name):
        r"""Sets the crl_name of this CrlConfiguration.

        吊销列表文件名称。 > 若用户不指定，系统将默认采用当前证书的父CA ID。

        :param crl_name: The crl_name of this CrlConfiguration.
        :type crl_name: str
        """
        self._crl_name = crl_name

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this CrlConfiguration.

        OBS桶名称。 > 当需要启用CRL发布功能： > - 此参数为必填项，且用户必须已创建委托授权，授予PCA服务对OBS的相关权限，具体参见本文档：**证书吊销处理>查看是否具有委托权限**、**证书吊销处理>创建委托**； > - 指定的OBS桶必须存在，否则将报错。

        :return: The obs_bucket_name of this CrlConfiguration.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this CrlConfiguration.

        OBS桶名称。 > 当需要启用CRL发布功能： > - 此参数为必填项，且用户必须已创建委托授权，授予PCA服务对OBS的相关权限，具体参见本文档：**证书吊销处理>查看是否具有委托权限**、**证书吊销处理>创建委托**； > - 指定的OBS桶必须存在，否则将报错。

        :param obs_bucket_name: The obs_bucket_name of this CrlConfiguration.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def valid_days(self):
        r"""Gets the valid_days of this CrlConfiguration.

        CRL更新周期，单位为\"天\"。当启用CRL发布功能，为必填项。

        :return: The valid_days of this CrlConfiguration.
        :rtype: int
        """
        return self._valid_days

    @valid_days.setter
    def valid_days(self, valid_days):
        r"""Sets the valid_days of this CrlConfiguration.

        CRL更新周期，单位为\"天\"。当启用CRL发布功能，为必填项。

        :param valid_days: The valid_days of this CrlConfiguration.
        :type valid_days: int
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
