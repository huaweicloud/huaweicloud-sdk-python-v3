# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTransTemplateGroup:

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
        'status': 'str',
        'auto_encrypt': 'int',
        'quality_info_list': 'list[QualityInfo]',
        'watermark_template_ids': 'list[str]',
        'description': 'str',
        'common': 'Common'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'status': 'status',
        'auto_encrypt': 'auto_encrypt',
        'quality_info_list': 'quality_info_list',
        'watermark_template_ids': 'watermark_template_ids',
        'description': 'description',
        'common': 'common'
    }

    def __init__(self, group_id=None, name=None, status=None, auto_encrypt=None, quality_info_list=None, watermark_template_ids=None, description=None, common=None):
        """ModifyTransTemplateGroup

        The model defined in huaweicloud sdk

        :param group_id: 模板组名称。
        :type group_id: str
        :param name: 模板组名称。
        :type name: str
        :param status: 是否设置默认。
        :type status: str
        :param auto_encrypt: 是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。
        :type auto_encrypt: int
        :param quality_info_list: 画质配置信息列表。
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfo`]
        :param watermark_template_ids: 绑定的水印模板组ID数组。
        :type watermark_template_ids: list[str]
        :param description: 模板介绍。
        :type description: str
        :param common: 
        :type common: :class:`huaweicloudsdkvod.v1.Common`
        """
        
        

        self._group_id = None
        self._name = None
        self._status = None
        self._auto_encrypt = None
        self._quality_info_list = None
        self._watermark_template_ids = None
        self._description = None
        self._common = None
        self.discriminator = None

        self.group_id = group_id
        self.name = name
        if status is not None:
            self.status = status
        if auto_encrypt is not None:
            self.auto_encrypt = auto_encrypt
        if quality_info_list is not None:
            self.quality_info_list = quality_info_list
        if watermark_template_ids is not None:
            self.watermark_template_ids = watermark_template_ids
        if description is not None:
            self.description = description
        if common is not None:
            self.common = common

    @property
    def group_id(self):
        """Gets the group_id of this ModifyTransTemplateGroup.

        模板组名称。

        :return: The group_id of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ModifyTransTemplateGroup.

        模板组名称。

        :param group_id: The group_id of this ModifyTransTemplateGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ModifyTransTemplateGroup.

        模板组名称。

        :return: The name of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyTransTemplateGroup.

        模板组名称。

        :param name: The name of this ModifyTransTemplateGroup.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ModifyTransTemplateGroup.

        是否设置默认。

        :return: The status of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModifyTransTemplateGroup.

        是否设置默认。

        :param status: The status of this ModifyTransTemplateGroup.
        :type status: str
        """
        self._status = status

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this ModifyTransTemplateGroup.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :return: The auto_encrypt of this ModifyTransTemplateGroup.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this ModifyTransTemplateGroup.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :param auto_encrypt: The auto_encrypt of this ModifyTransTemplateGroup.
        :type auto_encrypt: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def quality_info_list(self):
        """Gets the quality_info_list of this ModifyTransTemplateGroup.

        画质配置信息列表。

        :return: The quality_info_list of this ModifyTransTemplateGroup.
        :rtype: list[:class:`huaweicloudsdkvod.v1.QualityInfo`]
        """
        return self._quality_info_list

    @quality_info_list.setter
    def quality_info_list(self, quality_info_list):
        """Sets the quality_info_list of this ModifyTransTemplateGroup.

        画质配置信息列表。

        :param quality_info_list: The quality_info_list of this ModifyTransTemplateGroup.
        :type quality_info_list: list[:class:`huaweicloudsdkvod.v1.QualityInfo`]
        """
        self._quality_info_list = quality_info_list

    @property
    def watermark_template_ids(self):
        """Gets the watermark_template_ids of this ModifyTransTemplateGroup.

        绑定的水印模板组ID数组。

        :return: The watermark_template_ids of this ModifyTransTemplateGroup.
        :rtype: list[str]
        """
        return self._watermark_template_ids

    @watermark_template_ids.setter
    def watermark_template_ids(self, watermark_template_ids):
        """Sets the watermark_template_ids of this ModifyTransTemplateGroup.

        绑定的水印模板组ID数组。

        :param watermark_template_ids: The watermark_template_ids of this ModifyTransTemplateGroup.
        :type watermark_template_ids: list[str]
        """
        self._watermark_template_ids = watermark_template_ids

    @property
    def description(self):
        """Gets the description of this ModifyTransTemplateGroup.

        模板介绍。

        :return: The description of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyTransTemplateGroup.

        模板介绍。

        :param description: The description of this ModifyTransTemplateGroup.
        :type description: str
        """
        self._description = description

    @property
    def common(self):
        """Gets the common of this ModifyTransTemplateGroup.

        :return: The common of this ModifyTransTemplateGroup.
        :rtype: :class:`huaweicloudsdkvod.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this ModifyTransTemplateGroup.

        :param common: The common of this ModifyTransTemplateGroup.
        :type common: :class:`huaweicloudsdkvod.v1.Common`
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
        if not isinstance(other, ModifyTransTemplateGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
