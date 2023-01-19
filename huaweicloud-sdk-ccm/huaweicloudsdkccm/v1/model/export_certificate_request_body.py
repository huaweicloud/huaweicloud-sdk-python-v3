# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_compressed': 'str',
        'type': 'str',
        'is_sm_standard': 'str'
    }

    attribute_map = {
        'is_compressed': 'is_compressed',
        'type': 'type',
        'is_sm_standard': 'is_sm_standard'
    }

    def __init__(self, is_compressed=None, type=None, is_sm_standard=None):
        """ExportCertificateRequestBody

        The model defined in huaweicloud sdk

        :param is_compressed: 是否压缩。   - **true**   - **false**
        :type is_compressed: str
        :param type: 根据服务器类型选择下载证书的形式，支持以下五种类型：   - **APACHE** : apache服务器推荐使用此参数；   - **NGINX** : nginx服务器推荐使用此参数；   - **IIS** : windows服务器推荐使用此参数；   - **TOMCAT** : tomcat服务器推荐使用此参数；   - **OTHER** : 下载PEM格式证书，推荐使用此参数。
        :type type: str
        :param is_sm_standard: 是否国密GMT0009标准规范。当证书算法为SM2时传入才有效，若不传入，则默认为false。   - **true**   - **false**
        :type is_sm_standard: str
        """
        
        

        self._is_compressed = None
        self._type = None
        self._is_sm_standard = None
        self.discriminator = None

        self.is_compressed = is_compressed
        self.type = type
        if is_sm_standard is not None:
            self.is_sm_standard = is_sm_standard

    @property
    def is_compressed(self):
        """Gets the is_compressed of this ExportCertificateRequestBody.

        是否压缩。   - **true**   - **false**

        :return: The is_compressed of this ExportCertificateRequestBody.
        :rtype: str
        """
        return self._is_compressed

    @is_compressed.setter
    def is_compressed(self, is_compressed):
        """Sets the is_compressed of this ExportCertificateRequestBody.

        是否压缩。   - **true**   - **false**

        :param is_compressed: The is_compressed of this ExportCertificateRequestBody.
        :type is_compressed: str
        """
        self._is_compressed = is_compressed

    @property
    def type(self):
        """Gets the type of this ExportCertificateRequestBody.

        根据服务器类型选择下载证书的形式，支持以下五种类型：   - **APACHE** : apache服务器推荐使用此参数；   - **NGINX** : nginx服务器推荐使用此参数；   - **IIS** : windows服务器推荐使用此参数；   - **TOMCAT** : tomcat服务器推荐使用此参数；   - **OTHER** : 下载PEM格式证书，推荐使用此参数。

        :return: The type of this ExportCertificateRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportCertificateRequestBody.

        根据服务器类型选择下载证书的形式，支持以下五种类型：   - **APACHE** : apache服务器推荐使用此参数；   - **NGINX** : nginx服务器推荐使用此参数；   - **IIS** : windows服务器推荐使用此参数；   - **TOMCAT** : tomcat服务器推荐使用此参数；   - **OTHER** : 下载PEM格式证书，推荐使用此参数。

        :param type: The type of this ExportCertificateRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def is_sm_standard(self):
        """Gets the is_sm_standard of this ExportCertificateRequestBody.

        是否国密GMT0009标准规范。当证书算法为SM2时传入才有效，若不传入，则默认为false。   - **true**   - **false**

        :return: The is_sm_standard of this ExportCertificateRequestBody.
        :rtype: str
        """
        return self._is_sm_standard

    @is_sm_standard.setter
    def is_sm_standard(self, is_sm_standard):
        """Sets the is_sm_standard of this ExportCertificateRequestBody.

        是否国密GMT0009标准规范。当证书算法为SM2时传入才有效，若不传入，则默认为false。   - **true**   - **false**

        :param is_sm_standard: The is_sm_standard of this ExportCertificateRequestBody.
        :type is_sm_standard: str
        """
        self._is_sm_standard = is_sm_standard

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
        if not isinstance(other, ExportCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
