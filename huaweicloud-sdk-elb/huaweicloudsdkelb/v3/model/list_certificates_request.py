# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'domain': 'list[str]',
        'type': 'list[str]',
        'scm_certificate_id': 'list[str]',
        'common_name': 'list[str]',
        'fingerprint': 'list[str]',
        'source': 'list[str]',
        'protection_status': 'list[str]',
        'protection_reason': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'domain': 'domain',
        'type': 'type',
        'scm_certificate_id': 'scm_certificate_id',
        'common_name': 'common_name',
        'fingerprint': 'fingerprint',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, admin_state_up=None, domain=None, type=None, scm_certificate_id=None, common_name=None, fingerprint=None, source=None, protection_status=None, protection_reason=None, enterprise_project_id=None):
        r"""ListCertificatesRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：证书ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：证书的名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param description: **参数解释**：证书的描述。 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param admin_state_up: **参数解释**：证书的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。  **默认取值**：不涉及
        :type admin_state_up: bool
        :param domain: **参数解释**：服务器证书所签域名。 支持多值查询，查询条件格式：domain&#x3D;xxx&amp;domain&#x3D;xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type domain: list[str]
        :param type: **参数解释**：证书的类型。 支持多值查询，查询条件格式：type&#x3D;xxx&amp;type&#x3D;xxx。  **约束限制**：不涉及  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。  **默认取值**：不涉及
        :type type: list[str]
        :param scm_certificate_id: **参数解释**：云证书管理服务（CCM）中的证书ID。 支持多值查询，查询条件格式：scm_certificate_id&#x3D;xxx&amp;scm_certificate_id&#x3D;xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type scm_certificate_id: list[str]
        :param common_name: **参数解释**：证书的主域名。 支持多值查询，查询条件格式：common_name&#x3D;xxx&amp;common_name&#x3D;xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type common_name: list[str]
        :param fingerprint: **参数解释**：证书的指纹。 支持多值查询，查询条件格式：fingerprint&#x3D;xxx&amp;fingerprint&#x3D;xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type fingerprint: list[str]
        :param source: **参数解释**：证书来源。 支持多值查询，查询条件格式：source&#x3D;xxx&amp;source&#x3D;xxx。  **约束限制**：不涉及  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及
        :type source: list[str]
        :param protection_status: **参数解释**：修改保护状态。 支持多值查询，查询条件格式：protection_status&#x3D;xxx&amp;protection_status&#x3D;xxx。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护，即禁止通过控制台修改。  **默认取值**：不涉及
        :type protection_status: list[str]
        :param protection_reason: **参数解释**：设置修改保护的原因。 支持多值查询，查询条件格式：protection_reason&#x3D;xxx&amp;protection_reason&#x3D;xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type protection_reason: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:certificates:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及
        :type enterprise_project_id: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._domain = None
        self._type = None
        self._scm_certificate_id = None
        self._common_name = None
        self._fingerprint = None
        self._source = None
        self._protection_status = None
        self._protection_reason = None
        self._enterprise_project_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        if common_name is not None:
            self.common_name = common_name
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if source is not None:
            self.source = source
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def marker(self):
        r"""Gets the marker of this ListCertificatesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCertificatesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListCertificatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListCertificatesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCertificatesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListCertificatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListCertificatesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListCertificatesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListCertificatesRequest.

        **参数解释**：证书ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCertificatesRequest.

        **参数解释**：证书ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListCertificatesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListCertificatesRequest.

        **参数解释**：证书的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCertificatesRequest.

        **参数解释**：证书的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListCertificatesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListCertificatesRequest.

        **参数解释**：证书的描述。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListCertificatesRequest.

        **参数解释**：证书的描述。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListCertificatesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListCertificatesRequest.

        **参数解释**：证书的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。  **默认取值**：不涉及

        :return: The admin_state_up of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListCertificatesRequest.

        **参数解释**：证书的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this ListCertificatesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def domain(self):
        r"""Gets the domain of this ListCertificatesRequest.

        **参数解释**：服务器证书所签域名。 支持多值查询，查询条件格式：domain=xxx&domain=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The domain of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListCertificatesRequest.

        **参数解释**：服务器证书所签域名。 支持多值查询，查询条件格式：domain=xxx&domain=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param domain: The domain of this ListCertificatesRequest.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def type(self):
        r"""Gets the type of this ListCertificatesRequest.

        **参数解释**：证书的类型。 支持多值查询，查询条件格式：type=xxx&type=xxx。  **约束限制**：不涉及  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。  **默认取值**：不涉及

        :return: The type of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCertificatesRequest.

        **参数解释**：证书的类型。 支持多值查询，查询条件格式：type=xxx&type=xxx。  **约束限制**：不涉及  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。  **默认取值**：不涉及

        :param type: The type of this ListCertificatesRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this ListCertificatesRequest.

        **参数解释**：云证书管理服务（CCM）中的证书ID。 支持多值查询，查询条件格式：scm_certificate_id=xxx&scm_certificate_id=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The scm_certificate_id of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this ListCertificatesRequest.

        **参数解释**：云证书管理服务（CCM）中的证书ID。 支持多值查询，查询条件格式：scm_certificate_id=xxx&scm_certificate_id=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param scm_certificate_id: The scm_certificate_id of this ListCertificatesRequest.
        :type scm_certificate_id: list[str]
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def common_name(self):
        r"""Gets the common_name of this ListCertificatesRequest.

        **参数解释**：证书的主域名。 支持多值查询，查询条件格式：common_name=xxx&common_name=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The common_name of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this ListCertificatesRequest.

        **参数解释**：证书的主域名。 支持多值查询，查询条件格式：common_name=xxx&common_name=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param common_name: The common_name of this ListCertificatesRequest.
        :type common_name: list[str]
        """
        self._common_name = common_name

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this ListCertificatesRequest.

        **参数解释**：证书的指纹。 支持多值查询，查询条件格式：fingerprint=xxx&fingerprint=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The fingerprint of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this ListCertificatesRequest.

        **参数解释**：证书的指纹。 支持多值查询，查询条件格式：fingerprint=xxx&fingerprint=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param fingerprint: The fingerprint of this ListCertificatesRequest.
        :type fingerprint: list[str]
        """
        self._fingerprint = fingerprint

    @property
    def source(self):
        r"""Gets the source of this ListCertificatesRequest.

        **参数解释**：证书来源。 支持多值查询，查询条件格式：source=xxx&source=xxx。  **约束限制**：不涉及  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及

        :return: The source of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListCertificatesRequest.

        **参数解释**：证书来源。 支持多值查询，查询条件格式：source=xxx&source=xxx。  **约束限制**：不涉及  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及

        :param source: The source of this ListCertificatesRequest.
        :type source: list[str]
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ListCertificatesRequest.

        **参数解释**：修改保护状态。 支持多值查询，查询条件格式：protection_status=xxx&protection_status=xxx。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护，即禁止通过控制台修改。  **默认取值**：不涉及

        :return: The protection_status of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ListCertificatesRequest.

        **参数解释**：修改保护状态。 支持多值查询，查询条件格式：protection_status=xxx&protection_status=xxx。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护，即禁止通过控制台修改。  **默认取值**：不涉及

        :param protection_status: The protection_status of this ListCertificatesRequest.
        :type protection_status: list[str]
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this ListCertificatesRequest.

        **参数解释**：设置修改保护的原因。 支持多值查询，查询条件格式：protection_reason=xxx&protection_reason=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The protection_reason of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this ListCertificatesRequest.

        **参数解释**：设置修改保护的原因。 支持多值查询，查询条件格式：protection_reason=xxx&protection_reason=xxx。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param protection_reason: The protection_reason of this ListCertificatesRequest.
        :type protection_reason: list[str]
        """
        self._protection_reason = protection_reason

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCertificatesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:certificates:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The enterprise_project_id of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCertificatesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:certificates:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListCertificatesRequest.
        :type enterprise_project_id: list[str]
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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
