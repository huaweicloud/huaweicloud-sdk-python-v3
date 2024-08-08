# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerImageReq:

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
        'description': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None):
        """CreateServerImageReq

        The model defined in huaweicloud sdk

        :param name: 镜像名称，名称需满足如下规则: * 首尾字符不能为空格。 * 长度范围1～128个字符。 * 只允许3种字符，英文大小写，数字，特殊字符包含-、.、_、空格和中文。
        :type name: str
        :param description: 镜像描述，描述需满足如下规则: * 首字符不能为空格。 * 长度范围0～1024个字符。 * 支持字母、数字、中文。 * 不支持回车、&lt;、 &gt;字符。
        :type description: str
        :param enterprise_project_id: **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateServerImageReq.

        镜像名称，名称需满足如下规则: * 首尾字符不能为空格。 * 长度范围1～128个字符。 * 只允许3种字符，英文大小写，数字，特殊字符包含-、.、_、空格和中文。

        :return: The name of this CreateServerImageReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateServerImageReq.

        镜像名称，名称需满足如下规则: * 首尾字符不能为空格。 * 长度范围1～128个字符。 * 只允许3种字符，英文大小写，数字，特殊字符包含-、.、_、空格和中文。

        :param name: The name of this CreateServerImageReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateServerImageReq.

        镜像描述，描述需满足如下规则: * 首字符不能为空格。 * 长度范围0～1024个字符。 * 支持字母、数字、中文。 * 不支持回车、<、 >字符。

        :return: The description of this CreateServerImageReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateServerImageReq.

        镜像描述，描述需满足如下规则: * 首字符不能为空格。 * 长度范围0～1024个字符。 * 支持字母、数字、中文。 * 不支持回车、<、 >字符。

        :param description: The description of this CreateServerImageReq.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateServerImageReq.

        **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。

        :return: The enterprise_project_id of this CreateServerImageReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateServerImageReq.

        **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。

        :param enterprise_project_id: The enterprise_project_id of this CreateServerImageReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateServerImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
