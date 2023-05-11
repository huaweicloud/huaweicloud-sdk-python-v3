# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTransTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'name': 'str',
        'is_default': 'bool',
        'is_auto_encrypt': 'bool',
        'quality_info_list': 'list[QualityInfoList]',
        'watermark_template_ids': 'list[str]',
        'description': 'str',
        'common': 'CommonInfo'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'is_default': 'is_default',
        'is_auto_encrypt': 'is_auto_encrypt',
        'quality_info_list': 'quality_info_list',
        'watermark_template_ids': 'watermark_template_ids',
        'description': 'description',
        'common': 'common'
    }

    def __init__(self, group_id=None, name=None, is_default=None, is_auto_encrypt=None, quality_info_list=None, watermark_template_ids=None, description=None, common=None):
        """ModifyTransTemplate

        The model defined in huaweicloud sdk

        :param group_id: 模板组名称&lt;br/&gt; 
        :type group_id: str
        :param name: 模板组名称&lt;br/&gt; 
        :type name: str
        :param is_default: 是否是默认转码模板&lt;br/&gt; 
        :type is_default: bool
        :param is_auto_encrypt: 是否开启加密
        :type is_auto_encrypt: bool
        :param quality_info_list: 画质配置信息列表&lt;br/&gt; 
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        :param watermark_template_ids: 绑定的水印模板组ID数组&lt;br/&gt; 
        :type watermark_template_ids: list[str]
        :param description: 模板介绍&lt;br/&gt; 
        :type description: str
        :param common: 
        :type common: :class:`huaweicloudsdkvod.v1.CommonInfo`
        """
        
        

        self._group_id = None
        self._name = None
        self._is_default = None
        self._is_auto_encrypt = None
        self._quality_info_list = None
        self._watermark_template_ids = None
        self._description = None
        self._common = None
        self.discriminator = None

        self.group_id = group_id
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if is_auto_encrypt is not None:
            self.is_auto_encrypt = is_auto_encrypt
        self.quality_info_list = quality_info_list
        if watermark_template_ids is not None:
            self.watermark_template_ids = watermark_template_ids
        if description is not None:
            self.description = description
        self.common = common

    @property
    def group_id(self):
        """Gets the group_id of this ModifyTransTemplate.

        模板组名称<br/> 

        :return: The group_id of this ModifyTransTemplate.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ModifyTransTemplate.

        模板组名称<br/> 

        :param group_id: The group_id of this ModifyTransTemplate.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ModifyTransTemplate.

        模板组名称<br/> 

        :return: The name of this ModifyTransTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyTransTemplate.

        模板组名称<br/> 

        :param name: The name of this ModifyTransTemplate.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this ModifyTransTemplate.

        是否是默认转码模板<br/> 

        :return: The is_default of this ModifyTransTemplate.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this ModifyTransTemplate.

        是否是默认转码模板<br/> 

        :param is_default: The is_default of this ModifyTransTemplate.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def is_auto_encrypt(self):
        """Gets the is_auto_encrypt of this ModifyTransTemplate.

        是否开启加密

        :return: The is_auto_encrypt of this ModifyTransTemplate.
        :rtype: bool
        """
        return self._is_auto_encrypt

    @is_auto_encrypt.setter
    def is_auto_encrypt(self, is_auto_encrypt):
        """Sets the is_auto_encrypt of this ModifyTransTemplate.

        是否开启加密

        :param is_auto_encrypt: The is_auto_encrypt of this ModifyTransTemplate.
        :type is_auto_encrypt: bool
        """
        self._is_auto_encrypt = is_auto_encrypt

    @property
    def quality_info_list(self):
        """Gets the quality_info_list of this ModifyTransTemplate.

        画质配置信息列表<br/> 

        :return: The quality_info_list of this ModifyTransTemplate.
        :rtype: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        """
        return self._quality_info_list

    @quality_info_list.setter
    def quality_info_list(self, quality_info_list):
        """Sets the quality_info_list of this ModifyTransTemplate.

        画质配置信息列表<br/> 

        :param quality_info_list: The quality_info_list of this ModifyTransTemplate.
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfoList`]
        """
        self._quality_info_list = quality_info_list

    @property
    def watermark_template_ids(self):
        """Gets the watermark_template_ids of this ModifyTransTemplate.

        绑定的水印模板组ID数组<br/> 

        :return: The watermark_template_ids of this ModifyTransTemplate.
        :rtype: list[str]
        """
        return self._watermark_template_ids

    @watermark_template_ids.setter
    def watermark_template_ids(self, watermark_template_ids):
        """Sets the watermark_template_ids of this ModifyTransTemplate.

        绑定的水印模板组ID数组<br/> 

        :param watermark_template_ids: The watermark_template_ids of this ModifyTransTemplate.
        :type watermark_template_ids: list[str]
        """
        self._watermark_template_ids = watermark_template_ids

    @property
    def description(self):
        """Gets the description of this ModifyTransTemplate.

        模板介绍<br/> 

        :return: The description of this ModifyTransTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyTransTemplate.

        模板介绍<br/> 

        :param description: The description of this ModifyTransTemplate.
        :type description: str
        """
        self._description = description

    @property
    def common(self):
        """Gets the common of this ModifyTransTemplate.

        :return: The common of this ModifyTransTemplate.
        :rtype: :class:`huaweicloudsdkvod.v1.CommonInfo`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this ModifyTransTemplate.

        :param common: The common of this ModifyTransTemplate.
        :type common: :class:`huaweicloudsdkvod.v1.CommonInfo`
        """
        self._common = common

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
        if not isinstance(other, ModifyTransTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
