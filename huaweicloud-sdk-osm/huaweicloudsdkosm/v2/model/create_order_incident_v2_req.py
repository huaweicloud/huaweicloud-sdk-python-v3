# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrderIncidentV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_sub_type_id': 'str',
        'product_category_id': 'str',
        'business_type_id': 'str',
        'region_id': 'str',
        'simple_description': 'str',
        'source_id': 'str',
        'is_authorized': 'int',
        'authorization_content': 'str',
        'remind_mobile': 'str',
        'remind_mail': 'str',
        'remind_time': 'str',
        'project_id': 'str',
        'accessory_ids': 'list[str]',
        'extends_map': 'dict(str, object)',
        'extension_map': 'dict(str, object)',
        'severity_id': 'str',
        'verify_code': 'str',
        'area_code': 'str'
    }

    attribute_map = {
        'incident_sub_type_id': 'incident_sub_type_id',
        'product_category_id': 'product_category_id',
        'business_type_id': 'business_type_id',
        'region_id': 'region_id',
        'simple_description': 'simple_description',
        'source_id': 'source_id',
        'is_authorized': 'is_authorized',
        'authorization_content': 'authorization_content',
        'remind_mobile': 'remind_mobile',
        'remind_mail': 'remind_mail',
        'remind_time': 'remind_time',
        'project_id': 'project_id',
        'accessory_ids': 'accessory_ids',
        'extends_map': 'extends_map',
        'extension_map': 'extension_map',
        'severity_id': 'severity_id',
        'verify_code': 'verify_code',
        'area_code': 'area_code'
    }

    def __init__(self, incident_sub_type_id=None, product_category_id=None, business_type_id=None, region_id=None, simple_description=None, source_id=None, is_authorized=None, authorization_content=None, remind_mobile=None, remind_mail=None, remind_time=None, project_id=None, accessory_ids=None, extends_map=None, extension_map=None, severity_id=None, verify_code=None, area_code=None):
        """CreateOrderIncidentV2Req

        The model defined in huaweicloud sdk

        :param incident_sub_type_id: 工单子类
        :type incident_sub_type_id: str
        :param product_category_id: 工单产品类型
        :type product_category_id: str
        :param business_type_id: 工单问题类型
        :type business_type_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param simple_description: 问题描述
        :type simple_description: str
        :param source_id: 工单来源，当前固定为83aeb0f2834c4df49826c781d32a963e
        :type source_id: str
        :param is_authorized: 是否授权
        :type is_authorized: int
        :param authorization_content: 机密信息内容
        :type authorization_content: str
        :param remind_mobile: 提醒手机号
        :type remind_mobile: str
        :param remind_mail: 提醒邮箱
        :type remind_mail: str
        :param remind_time: 提醒时间，如果是任意时间传0，如果是指定时间，传客户首选项对应时区的时间，比如09:00-18:00
        :type remind_time: str
        :param project_id: 项目id
        :type project_id: str
        :param accessory_ids: 附件id列表
        :type accessory_ids: list[str]
        :param extends_map: 附加参数
        :type extends_map: dict(str, object)
        :param extension_map: 扩展参数
        :type extension_map: dict(str, object)
        :param severity_id: 严重性id
        :type severity_id: str
        :param verify_code: 验证码
        :type verify_code: str
        :param area_code: 国家码
        :type area_code: str
        """
        
        

        self._incident_sub_type_id = None
        self._product_category_id = None
        self._business_type_id = None
        self._region_id = None
        self._simple_description = None
        self._source_id = None
        self._is_authorized = None
        self._authorization_content = None
        self._remind_mobile = None
        self._remind_mail = None
        self._remind_time = None
        self._project_id = None
        self._accessory_ids = None
        self._extends_map = None
        self._extension_map = None
        self._severity_id = None
        self._verify_code = None
        self._area_code = None
        self.discriminator = None

        if incident_sub_type_id is not None:
            self.incident_sub_type_id = incident_sub_type_id
        if product_category_id is not None:
            self.product_category_id = product_category_id
        self.business_type_id = business_type_id
        if region_id is not None:
            self.region_id = region_id
        self.simple_description = simple_description
        self.source_id = source_id
        if is_authorized is not None:
            self.is_authorized = is_authorized
        if authorization_content is not None:
            self.authorization_content = authorization_content
        if remind_mobile is not None:
            self.remind_mobile = remind_mobile
        if remind_mail is not None:
            self.remind_mail = remind_mail
        if remind_time is not None:
            self.remind_time = remind_time
        if project_id is not None:
            self.project_id = project_id
        if accessory_ids is not None:
            self.accessory_ids = accessory_ids
        if extends_map is not None:
            self.extends_map = extends_map
        if extension_map is not None:
            self.extension_map = extension_map
        if severity_id is not None:
            self.severity_id = severity_id
        if verify_code is not None:
            self.verify_code = verify_code
        if area_code is not None:
            self.area_code = area_code

    @property
    def incident_sub_type_id(self):
        """Gets the incident_sub_type_id of this CreateOrderIncidentV2Req.

        工单子类

        :return: The incident_sub_type_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._incident_sub_type_id

    @incident_sub_type_id.setter
    def incident_sub_type_id(self, incident_sub_type_id):
        """Sets the incident_sub_type_id of this CreateOrderIncidentV2Req.

        工单子类

        :param incident_sub_type_id: The incident_sub_type_id of this CreateOrderIncidentV2Req.
        :type incident_sub_type_id: str
        """
        self._incident_sub_type_id = incident_sub_type_id

    @property
    def product_category_id(self):
        """Gets the product_category_id of this CreateOrderIncidentV2Req.

        工单产品类型

        :return: The product_category_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._product_category_id

    @product_category_id.setter
    def product_category_id(self, product_category_id):
        """Sets the product_category_id of this CreateOrderIncidentV2Req.

        工单产品类型

        :param product_category_id: The product_category_id of this CreateOrderIncidentV2Req.
        :type product_category_id: str
        """
        self._product_category_id = product_category_id

    @property
    def business_type_id(self):
        """Gets the business_type_id of this CreateOrderIncidentV2Req.

        工单问题类型

        :return: The business_type_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this CreateOrderIncidentV2Req.

        工单问题类型

        :param business_type_id: The business_type_id of this CreateOrderIncidentV2Req.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def region_id(self):
        """Gets the region_id of this CreateOrderIncidentV2Req.

        区域ID

        :return: The region_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateOrderIncidentV2Req.

        区域ID

        :param region_id: The region_id of this CreateOrderIncidentV2Req.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def simple_description(self):
        """Gets the simple_description of this CreateOrderIncidentV2Req.

        问题描述

        :return: The simple_description of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this CreateOrderIncidentV2Req.

        问题描述

        :param simple_description: The simple_description of this CreateOrderIncidentV2Req.
        :type simple_description: str
        """
        self._simple_description = simple_description

    @property
    def source_id(self):
        """Gets the source_id of this CreateOrderIncidentV2Req.

        工单来源，当前固定为83aeb0f2834c4df49826c781d32a963e

        :return: The source_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CreateOrderIncidentV2Req.

        工单来源，当前固定为83aeb0f2834c4df49826c781d32a963e

        :param source_id: The source_id of this CreateOrderIncidentV2Req.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def is_authorized(self):
        """Gets the is_authorized of this CreateOrderIncidentV2Req.

        是否授权

        :return: The is_authorized of this CreateOrderIncidentV2Req.
        :rtype: int
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this CreateOrderIncidentV2Req.

        是否授权

        :param is_authorized: The is_authorized of this CreateOrderIncidentV2Req.
        :type is_authorized: int
        """
        self._is_authorized = is_authorized

    @property
    def authorization_content(self):
        """Gets the authorization_content of this CreateOrderIncidentV2Req.

        机密信息内容

        :return: The authorization_content of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._authorization_content

    @authorization_content.setter
    def authorization_content(self, authorization_content):
        """Sets the authorization_content of this CreateOrderIncidentV2Req.

        机密信息内容

        :param authorization_content: The authorization_content of this CreateOrderIncidentV2Req.
        :type authorization_content: str
        """
        self._authorization_content = authorization_content

    @property
    def remind_mobile(self):
        """Gets the remind_mobile of this CreateOrderIncidentV2Req.

        提醒手机号

        :return: The remind_mobile of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._remind_mobile

    @remind_mobile.setter
    def remind_mobile(self, remind_mobile):
        """Sets the remind_mobile of this CreateOrderIncidentV2Req.

        提醒手机号

        :param remind_mobile: The remind_mobile of this CreateOrderIncidentV2Req.
        :type remind_mobile: str
        """
        self._remind_mobile = remind_mobile

    @property
    def remind_mail(self):
        """Gets the remind_mail of this CreateOrderIncidentV2Req.

        提醒邮箱

        :return: The remind_mail of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._remind_mail

    @remind_mail.setter
    def remind_mail(self, remind_mail):
        """Sets the remind_mail of this CreateOrderIncidentV2Req.

        提醒邮箱

        :param remind_mail: The remind_mail of this CreateOrderIncidentV2Req.
        :type remind_mail: str
        """
        self._remind_mail = remind_mail

    @property
    def remind_time(self):
        """Gets the remind_time of this CreateOrderIncidentV2Req.

        提醒时间，如果是任意时间传0，如果是指定时间，传客户首选项对应时区的时间，比如09:00-18:00

        :return: The remind_time of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._remind_time

    @remind_time.setter
    def remind_time(self, remind_time):
        """Sets the remind_time of this CreateOrderIncidentV2Req.

        提醒时间，如果是任意时间传0，如果是指定时间，传客户首选项对应时区的时间，比如09:00-18:00

        :param remind_time: The remind_time of this CreateOrderIncidentV2Req.
        :type remind_time: str
        """
        self._remind_time = remind_time

    @property
    def project_id(self):
        """Gets the project_id of this CreateOrderIncidentV2Req.

        项目id

        :return: The project_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateOrderIncidentV2Req.

        项目id

        :param project_id: The project_id of this CreateOrderIncidentV2Req.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def accessory_ids(self):
        """Gets the accessory_ids of this CreateOrderIncidentV2Req.

        附件id列表

        :return: The accessory_ids of this CreateOrderIncidentV2Req.
        :rtype: list[str]
        """
        return self._accessory_ids

    @accessory_ids.setter
    def accessory_ids(self, accessory_ids):
        """Sets the accessory_ids of this CreateOrderIncidentV2Req.

        附件id列表

        :param accessory_ids: The accessory_ids of this CreateOrderIncidentV2Req.
        :type accessory_ids: list[str]
        """
        self._accessory_ids = accessory_ids

    @property
    def extends_map(self):
        """Gets the extends_map of this CreateOrderIncidentV2Req.

        附加参数

        :return: The extends_map of this CreateOrderIncidentV2Req.
        :rtype: dict(str, object)
        """
        return self._extends_map

    @extends_map.setter
    def extends_map(self, extends_map):
        """Sets the extends_map of this CreateOrderIncidentV2Req.

        附加参数

        :param extends_map: The extends_map of this CreateOrderIncidentV2Req.
        :type extends_map: dict(str, object)
        """
        self._extends_map = extends_map

    @property
    def extension_map(self):
        """Gets the extension_map of this CreateOrderIncidentV2Req.

        扩展参数

        :return: The extension_map of this CreateOrderIncidentV2Req.
        :rtype: dict(str, object)
        """
        return self._extension_map

    @extension_map.setter
    def extension_map(self, extension_map):
        """Sets the extension_map of this CreateOrderIncidentV2Req.

        扩展参数

        :param extension_map: The extension_map of this CreateOrderIncidentV2Req.
        :type extension_map: dict(str, object)
        """
        self._extension_map = extension_map

    @property
    def severity_id(self):
        """Gets the severity_id of this CreateOrderIncidentV2Req.

        严重性id

        :return: The severity_id of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        """Sets the severity_id of this CreateOrderIncidentV2Req.

        严重性id

        :param severity_id: The severity_id of this CreateOrderIncidentV2Req.
        :type severity_id: str
        """
        self._severity_id = severity_id

    @property
    def verify_code(self):
        """Gets the verify_code of this CreateOrderIncidentV2Req.

        验证码

        :return: The verify_code of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        """Sets the verify_code of this CreateOrderIncidentV2Req.

        验证码

        :param verify_code: The verify_code of this CreateOrderIncidentV2Req.
        :type verify_code: str
        """
        self._verify_code = verify_code

    @property
    def area_code(self):
        """Gets the area_code of this CreateOrderIncidentV2Req.

        国家码

        :return: The area_code of this CreateOrderIncidentV2Req.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this CreateOrderIncidentV2Req.

        国家码

        :param area_code: The area_code of this CreateOrderIncidentV2Req.
        :type area_code: str
        """
        self._area_code = area_code

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
        if not isinstance(other, CreateOrderIncidentV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
