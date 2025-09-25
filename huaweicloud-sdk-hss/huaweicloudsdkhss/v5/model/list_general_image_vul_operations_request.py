# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeneralImageVulOperationsRequest:

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
        'vul_id': 'str',
        'image_id': 'str',
        'image_type': 'str',
        'image_name': 'str',
        'status': 'str',
        'user_name': 'str',
        'handle_type': 'str',
        'app_name': 'str',
        'app_version': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'vul_id': 'vul_id',
        'image_id': 'image_id',
        'image_type': 'image_type',
        'image_name': 'image_name',
        'status': 'status',
        'user_name': 'user_name',
        'handle_type': 'handle_type',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'remark': 'remark'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, vul_id=None, image_id=None, image_type=None, image_name=None, status=None, user_name=None, handle_type=None, app_name=None, app_version=None, remark=None):
        r"""ListGeneralImageVulOperationsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param vul_id: **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param image_id: **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type image_id: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像  **默认取值**: 不涉及
        :type image_type: str
        :param image_name: 镜像名称
        :type image_name: str
        :param status: **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及
        :type status: str
        :param user_name: **参数解释**: 处理用户名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type user_name: str
        :param handle_type: **参数解释**: 操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore:：取消忽略 - add_to_whitelist：加入白名单  **默认取值**: 不涉及
        :type handle_type: str
        :param app_name: **参数解释**: 应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type app_name: str
        :param app_version: **参数解释**: 应用版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type app_version: str
        :param remark: **参数解释**: 备注 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type remark: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._vul_id = None
        self._image_id = None
        self._image_type = None
        self._image_name = None
        self._status = None
        self._user_name = None
        self._handle_type = None
        self._app_name = None
        self._app_version = None
        self._remark = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.vul_id = vul_id
        if image_id is not None:
            self.image_id = image_id
        self.image_type = image_type
        if image_name is not None:
            self.image_name = image_name
        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if handle_type is not None:
            self.handle_type = handle_type
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if remark is not None:
            self.remark = remark

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListGeneralImageVulOperationsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListGeneralImageVulOperationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListGeneralImageVulOperationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListGeneralImageVulOperationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListGeneralImageVulOperationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListGeneralImageVulOperationsRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The image_id of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListGeneralImageVulOperationsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像  **默认取值**: 不涉及

        :return: The image_type of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像  **默认取值**: 不涉及

        :param image_type: The image_type of this ListGeneralImageVulOperationsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_name(self):
        r"""Gets the image_name of this ListGeneralImageVulOperationsRequest.

        镜像名称

        :return: The image_name of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListGeneralImageVulOperationsRequest.

        镜像名称

        :param image_name: The image_name of this ListGeneralImageVulOperationsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def status(self):
        r"""Gets the status of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及

        :return: The status of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及

        :param status: The status of this ListGeneralImageVulOperationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def user_name(self):
        r"""Gets the user_name of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 处理用户名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The user_name of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 处理用户名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param user_name: The user_name of this ListGeneralImageVulOperationsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def handle_type(self):
        r"""Gets the handle_type of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore:：取消忽略 - add_to_whitelist：加入白名单  **默认取值**: 不涉及

        :return: The handle_type of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore:：取消忽略 - add_to_whitelist：加入白名单  **默认取值**: 不涉及

        :param handle_type: The handle_type of this ListGeneralImageVulOperationsRequest.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def app_name(self):
        r"""Gets the app_name of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The app_name of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param app_name: The app_name of this ListGeneralImageVulOperationsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 应用版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The app_version of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 应用版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param app_version: The app_version of this ListGeneralImageVulOperationsRequest.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def remark(self):
        r"""Gets the remark of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 备注 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The remark of this ListGeneralImageVulOperationsRequest.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ListGeneralImageVulOperationsRequest.

        **参数解释**: 备注 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param remark: The remark of this ListGeneralImageVulOperationsRequest.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, ListGeneralImageVulOperationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
