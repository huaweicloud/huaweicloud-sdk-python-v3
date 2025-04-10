# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCrlConfiguration:

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
        'valid_days': 'int',
        'crl_dis_point': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'crl_name': 'crl_name',
        'obs_bucket_name': 'obs_bucket_name',
        'valid_days': 'valid_days',
        'crl_dis_point': 'crl_dis_point'
    }

    def __init__(self, enabled=None, crl_name=None, obs_bucket_name=None, valid_days=None, crl_dis_point=None):
        r"""ListCrlConfiguration

        The model defined in huaweicloud sdk

        :param enabled: 是否启用CRL发布功能。 - **true** - **false**
        :type enabled: bool
        :param crl_name: 吊销列表文件名称。 &gt; 若用户不指定，系统将默认采用当前证书的父CA ID。
        :type crl_name: str
        :param obs_bucket_name: OBS桶名称。
        :type obs_bucket_name: str
        :param valid_days: CRL更新周期，单位为\&quot;天\&quot;。当启用CRL发布功能，为必填项。
        :type valid_days: int
        :param crl_dis_point: 吊销列表分发地址，即对应的OBS桶中的CRL文件地址。 &gt; 本参数由程序根据crl_name、obs_bucket_name以及OBS地址进行拼接而成。
        :type crl_dis_point: str
        """
        
        

        self._enabled = None
        self._crl_name = None
        self._obs_bucket_name = None
        self._valid_days = None
        self._crl_dis_point = None
        self.discriminator = None

        self.enabled = enabled
        self.crl_name = crl_name
        self.obs_bucket_name = obs_bucket_name
        self.valid_days = valid_days
        self.crl_dis_point = crl_dis_point

    @property
    def enabled(self):
        r"""Gets the enabled of this ListCrlConfiguration.

        是否启用CRL发布功能。 - **true** - **false**

        :return: The enabled of this ListCrlConfiguration.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListCrlConfiguration.

        是否启用CRL发布功能。 - **true** - **false**

        :param enabled: The enabled of this ListCrlConfiguration.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def crl_name(self):
        r"""Gets the crl_name of this ListCrlConfiguration.

        吊销列表文件名称。 > 若用户不指定，系统将默认采用当前证书的父CA ID。

        :return: The crl_name of this ListCrlConfiguration.
        :rtype: str
        """
        return self._crl_name

    @crl_name.setter
    def crl_name(self, crl_name):
        r"""Sets the crl_name of this ListCrlConfiguration.

        吊销列表文件名称。 > 若用户不指定，系统将默认采用当前证书的父CA ID。

        :param crl_name: The crl_name of this ListCrlConfiguration.
        :type crl_name: str
        """
        self._crl_name = crl_name

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ListCrlConfiguration.

        OBS桶名称。

        :return: The obs_bucket_name of this ListCrlConfiguration.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ListCrlConfiguration.

        OBS桶名称。

        :param obs_bucket_name: The obs_bucket_name of this ListCrlConfiguration.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def valid_days(self):
        r"""Gets the valid_days of this ListCrlConfiguration.

        CRL更新周期，单位为\"天\"。当启用CRL发布功能，为必填项。

        :return: The valid_days of this ListCrlConfiguration.
        :rtype: int
        """
        return self._valid_days

    @valid_days.setter
    def valid_days(self, valid_days):
        r"""Sets the valid_days of this ListCrlConfiguration.

        CRL更新周期，单位为\"天\"。当启用CRL发布功能，为必填项。

        :param valid_days: The valid_days of this ListCrlConfiguration.
        :type valid_days: int
        """
        self._valid_days = valid_days

    @property
    def crl_dis_point(self):
        r"""Gets the crl_dis_point of this ListCrlConfiguration.

        吊销列表分发地址，即对应的OBS桶中的CRL文件地址。 > 本参数由程序根据crl_name、obs_bucket_name以及OBS地址进行拼接而成。

        :return: The crl_dis_point of this ListCrlConfiguration.
        :rtype: str
        """
        return self._crl_dis_point

    @crl_dis_point.setter
    def crl_dis_point(self, crl_dis_point):
        r"""Sets the crl_dis_point of this ListCrlConfiguration.

        吊销列表分发地址，即对应的OBS桶中的CRL文件地址。 > 本参数由程序根据crl_name、obs_bucket_name以及OBS地址进行拼接而成。

        :param crl_dis_point: The crl_dis_point of this ListCrlConfiguration.
        :type crl_dis_point: str
        """
        self._crl_dis_point = crl_dis_point

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
        if not isinstance(other, ListCrlConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
