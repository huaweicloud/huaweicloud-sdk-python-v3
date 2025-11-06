# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLocalImageAppInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'image_id': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_id': 'image_id',
        'app_name': 'app_name'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_id=None, app_name=None):
        r"""ListLocalImageAppInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_id: **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_id: str
        :param app_name: **参数解释**: 软件名称过滤查询(支持模糊匹配) **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type app_name: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_id = None
        self._app_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_id = image_id
        if app_name is not None:
            self.app_name = app_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLocalImageAppInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListLocalImageAppInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLocalImageAppInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListLocalImageAppInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListLocalImageAppInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListLocalImageAppInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLocalImageAppInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListLocalImageAppInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLocalImageAppInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListLocalImageAppInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLocalImageAppInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListLocalImageAppInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_id(self):
        r"""Gets the image_id of this ListLocalImageAppInfoRequest.

        **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_id of this ListLocalImageAppInfoRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListLocalImageAppInfoRequest.

        **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListLocalImageAppInfoRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ListLocalImageAppInfoRequest.

        **参数解释**: 软件名称过滤查询(支持模糊匹配) **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The app_name of this ListLocalImageAppInfoRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListLocalImageAppInfoRequest.

        **参数解释**: 软件名称过滤查询(支持模糊匹配) **约束限制**： 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param app_name: The app_name of this ListLocalImageAppInfoRequest.
        :type app_name: str
        """
        self._app_name = app_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListLocalImageAppInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
