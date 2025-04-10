# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStyleRequestBody:

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
        'project_id': 'str',
        'status': 'str',
        'sex': 'str',
        'tags': 'list[str]',
        'style_assets': 'list[StyleAssetItem]',
        'extra_meta': 'StyleExtraMeta'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'status': 'status',
        'sex': 'sex',
        'tags': 'tags',
        'style_assets': 'style_assets',
        'extra_meta': 'extra_meta'
    }

    def __init__(self, name=None, description=None, project_id=None, status=None, sex=None, tags=None, style_assets=None, extra_meta=None):
        r"""CreateStyleRequestBody

        The model defined in huaweicloud sdk

        :param name: 数字人风格化名称
        :type name: str
        :param description: 数字人风格化描述
        :type description: str
        :param project_id: 租户ID
        :type project_id: str
        :param status: 状态
        :type status: str
        :param sex: 性别
        :type sex: str
        :param tags: 标签。单个标签16字节，多个用逗号分隔，最多50个。
        :type tags: list[str]
        :param style_assets: 风格化素材资产组合。
        :type style_assets: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        :param extra_meta: 
        :type extra_meta: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        """
        
        

        self._name = None
        self._description = None
        self._project_id = None
        self._status = None
        self._sex = None
        self._tags = None
        self._style_assets = None
        self._extra_meta = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if sex is not None:
            self.sex = sex
        if tags is not None:
            self.tags = tags
        if style_assets is not None:
            self.style_assets = style_assets
        if extra_meta is not None:
            self.extra_meta = extra_meta

    @property
    def name(self):
        r"""Gets the name of this CreateStyleRequestBody.

        数字人风格化名称

        :return: The name of this CreateStyleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateStyleRequestBody.

        数字人风格化名称

        :param name: The name of this CreateStyleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateStyleRequestBody.

        数字人风格化描述

        :return: The description of this CreateStyleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateStyleRequestBody.

        数字人风格化描述

        :param description: The description of this CreateStyleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateStyleRequestBody.

        租户ID

        :return: The project_id of this CreateStyleRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateStyleRequestBody.

        租户ID

        :param project_id: The project_id of this CreateStyleRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this CreateStyleRequestBody.

        状态

        :return: The status of this CreateStyleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateStyleRequestBody.

        状态

        :param status: The status of this CreateStyleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def sex(self):
        r"""Gets the sex of this CreateStyleRequestBody.

        性别

        :return: The sex of this CreateStyleRequestBody.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this CreateStyleRequestBody.

        性别

        :param sex: The sex of this CreateStyleRequestBody.
        :type sex: str
        """
        self._sex = sex

    @property
    def tags(self):
        r"""Gets the tags of this CreateStyleRequestBody.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :return: The tags of this CreateStyleRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateStyleRequestBody.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :param tags: The tags of this CreateStyleRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def style_assets(self):
        r"""Gets the style_assets of this CreateStyleRequestBody.

        风格化素材资产组合。

        :return: The style_assets of this CreateStyleRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        """
        return self._style_assets

    @style_assets.setter
    def style_assets(self, style_assets):
        r"""Sets the style_assets of this CreateStyleRequestBody.

        风格化素材资产组合。

        :param style_assets: The style_assets of this CreateStyleRequestBody.
        :type style_assets: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        """
        self._style_assets = style_assets

    @property
    def extra_meta(self):
        r"""Gets the extra_meta of this CreateStyleRequestBody.

        :return: The extra_meta of this CreateStyleRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        """
        return self._extra_meta

    @extra_meta.setter
    def extra_meta(self, extra_meta):
        r"""Sets the extra_meta of this CreateStyleRequestBody.

        :param extra_meta: The extra_meta of this CreateStyleRequestBody.
        :type extra_meta: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        """
        self._extra_meta = extra_meta

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
        if not isinstance(other, CreateStyleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
