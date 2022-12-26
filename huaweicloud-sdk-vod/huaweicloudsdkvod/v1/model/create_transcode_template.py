# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTranscodeTemplate:

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
        'is_default': 'bool',
        'is_auto_encrypt': 'bool',
        'quality_info_list': 'list[QualityInfoList]',
        'common': 'CommonInfo',
        'watermark_template_ids': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_default': 'is_default',
        'is_auto_encrypt': 'is_auto_encrypt',
        'quality_info_list': 'quality_info_list',
        'common': 'common',
        'watermark_template_ids': 'watermark_template_ids',
        'description': 'description'
    }

    def __init__(self, name=None, is_default=None, is_auto_encrypt=None, quality_info_list=None, common=None, watermark_template_ids=None, description=None):
        """CreateTranscodeTemplate

        The model defined in huaweicloud sdk

        :param name: 模板组名称&lt;br/&gt; 
        :type name: str
        :param is_default: 是否设置成默认转码模板&lt;br/&gt; 
        :type is_default: bool
        :param is_auto_encrypt: 是否开启加密
        :type is_auto_encrypt: bool
        :param quality_info_list: 画质配置信息列表&lt;br/&gt; 
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        :param common: 
        :type common: :class:`huaweicloudsdkvod.v1.CommonInfo`
        :param watermark_template_ids: 绑定的水印模板组ID数组&lt;br/&gt; 
        :type watermark_template_ids: list[str]
        :param description: 模板介绍&lt;br/&gt; 
        :type description: str
        """
        
        

        self._name = None
        self._is_default = None
        self._is_auto_encrypt = None
        self._quality_info_list = None
        self._common = None
        self._watermark_template_ids = None
        self._description = None
        self.discriminator = None

        self.name = name
        if is_default is not None:
            self.is_default = is_default
        if is_auto_encrypt is not None:
            self.is_auto_encrypt = is_auto_encrypt
        self.quality_info_list = quality_info_list
        self.common = common
        if watermark_template_ids is not None:
            self.watermark_template_ids = watermark_template_ids
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CreateTranscodeTemplate.

        模板组名称<br/> 

        :return: The name of this CreateTranscodeTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTranscodeTemplate.

        模板组名称<br/> 

        :param name: The name of this CreateTranscodeTemplate.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this CreateTranscodeTemplate.

        是否设置成默认转码模板<br/> 

        :return: The is_default of this CreateTranscodeTemplate.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CreateTranscodeTemplate.

        是否设置成默认转码模板<br/> 

        :param is_default: The is_default of this CreateTranscodeTemplate.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def is_auto_encrypt(self):
        """Gets the is_auto_encrypt of this CreateTranscodeTemplate.

        是否开启加密

        :return: The is_auto_encrypt of this CreateTranscodeTemplate.
        :rtype: bool
        """
        return self._is_auto_encrypt

    @is_auto_encrypt.setter
    def is_auto_encrypt(self, is_auto_encrypt):
        """Sets the is_auto_encrypt of this CreateTranscodeTemplate.

        是否开启加密

        :param is_auto_encrypt: The is_auto_encrypt of this CreateTranscodeTemplate.
        :type is_auto_encrypt: bool
        """
        self._is_auto_encrypt = is_auto_encrypt

    @property
    def quality_info_list(self):
        """Gets the quality_info_list of this CreateTranscodeTemplate.

        画质配置信息列表<br/> 

        :return: The quality_info_list of this CreateTranscodeTemplate.
        :rtype: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        """
        return self._quality_info_list

    @quality_info_list.setter
    def quality_info_list(self, quality_info_list):
        """Sets the quality_info_list of this CreateTranscodeTemplate.

        画质配置信息列表<br/> 

        :param quality_info_list: The quality_info_list of this CreateTranscodeTemplate.
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        """
        self._quality_info_list = quality_info_list

    @property
    def common(self):
        """Gets the common of this CreateTranscodeTemplate.

        :return: The common of this CreateTranscodeTemplate.
        :rtype: :class:`huaweicloudsdkvod.v1.CommonInfo`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this CreateTranscodeTemplate.

        :param common: The common of this CreateTranscodeTemplate.
        :type common: :class:`huaweicloudsdkvod.v1.CommonInfo`
        """
        self._common = common

    @property
    def watermark_template_ids(self):
        """Gets the watermark_template_ids of this CreateTranscodeTemplate.

        绑定的水印模板组ID数组<br/> 

        :return: The watermark_template_ids of this CreateTranscodeTemplate.
        :rtype: list[str]
        """
        return self._watermark_template_ids

    @watermark_template_ids.setter
    def watermark_template_ids(self, watermark_template_ids):
        """Sets the watermark_template_ids of this CreateTranscodeTemplate.

        绑定的水印模板组ID数组<br/> 

        :param watermark_template_ids: The watermark_template_ids of this CreateTranscodeTemplate.
        :type watermark_template_ids: list[str]
        """
        self._watermark_template_ids = watermark_template_ids

    @property
    def description(self):
        """Gets the description of this CreateTranscodeTemplate.

        模板介绍<br/> 

        :return: The description of this CreateTranscodeTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTranscodeTemplate.

        模板介绍<br/> 

        :param description: The description of this CreateTranscodeTemplate.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateTranscodeTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
