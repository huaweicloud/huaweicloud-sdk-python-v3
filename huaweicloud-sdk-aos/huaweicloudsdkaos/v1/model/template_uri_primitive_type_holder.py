# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateURIPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_uri': 'str'
    }

    attribute_map = {
        'template_uri': 'template_uri'
    }

    def __init__(self, template_uri=None):
        """TemplateURIPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param template_uri: HCL模板的OBS地址，该模板描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以“.tf”或者“.tf.json”结尾，并遵守HCL语法，且文件的编码格式须为UTF-8  压缩包目前只支持zip格式，文件需要以\&quot;.zip\&quot;结尾。解压后的文件不得包含\&quot;.tfvars\&quot;文件。解压前最大支持1MB，解压后最大支持1MB。zip压缩包文件数量不能超过100个  template_body和template_uri 必须有且只有一个存在  **注意：**   * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储template_uri对应的模板文件内容。   * template_uri对应的模板文件如果为zip类型，则内部的文件或文件夹名称长度不得超过255个字节，最深路径长度不得超过2048字节，zip包大小不得超过1MB
        :type template_uri: str
        """
        
        

        self._template_uri = None
        self.discriminator = None

        if template_uri is not None:
            self.template_uri = template_uri

    @property
    def template_uri(self):
        """Gets the template_uri of this TemplateURIPrimitiveTypeHolder.

        HCL模板的OBS地址，该模板描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以“.tf”或者“.tf.json”结尾，并遵守HCL语法，且文件的编码格式须为UTF-8  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件。解压前最大支持1MB，解压后最大支持1MB。zip压缩包文件数量不能超过100个  template_body和template_uri 必须有且只有一个存在  **注意：**   * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储template_uri对应的模板文件内容。   * template_uri对应的模板文件如果为zip类型，则内部的文件或文件夹名称长度不得超过255个字节，最深路径长度不得超过2048字节，zip包大小不得超过1MB

        :return: The template_uri of this TemplateURIPrimitiveTypeHolder.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this TemplateURIPrimitiveTypeHolder.

        HCL模板的OBS地址，该模板描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以“.tf”或者“.tf.json”结尾，并遵守HCL语法，且文件的编码格式须为UTF-8  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件。解压前最大支持1MB，解压后最大支持1MB。zip压缩包文件数量不能超过100个  template_body和template_uri 必须有且只有一个存在  **注意：**   * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储template_uri对应的模板文件内容。   * template_uri对应的模板文件如果为zip类型，则内部的文件或文件夹名称长度不得超过255个字节，最深路径长度不得超过2048字节，zip包大小不得超过1MB

        :param template_uri: The template_uri of this TemplateURIPrimitiveTypeHolder.
        :type template_uri: str
        """
        self._template_uri = template_uri

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
        if not isinstance(other, TemplateURIPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
