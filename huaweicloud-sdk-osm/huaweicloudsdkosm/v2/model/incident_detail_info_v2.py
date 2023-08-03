# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentDetailInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'xcustomer_id': 'str',
        'xcustomer_name': 'str',
        'status': 'int',
        'judgement': 'str',
        'incident_id': 'str',
        'business_type_name': 'str',
        'incident_type_name': 'str',
        'customer_id': 'str',
        'dc_name': 'str',
        'simple_description': 'str',
        'source_name': 'str',
        'create_time': 'datetime',
        'message_list': 'list[IncidentMessageV2]',
        'incident_satisfaction': 'list[IncidentSatisfactionV2Do]',
        'severity_name': 'str',
        'business_ownership': 'int',
        'resolve_time': 'int',
        'ext_info': 'IncidentDetailExtInfoV2'
    }

    attribute_map = {
        'xcustomer_id': 'xcustomer_id',
        'xcustomer_name': 'xcustomer_name',
        'status': 'status',
        'judgement': 'judgement',
        'incident_id': 'incident_id',
        'business_type_name': 'business_type_name',
        'incident_type_name': 'incident_type_name',
        'customer_id': 'customer_id',
        'dc_name': 'dc_name',
        'simple_description': 'simple_description',
        'source_name': 'source_name',
        'create_time': 'create_time',
        'message_list': 'message_list',
        'incident_satisfaction': 'incident_satisfaction',
        'severity_name': 'severity_name',
        'business_ownership': 'business_ownership',
        'resolve_time': 'resolve_time',
        'ext_info': 'ext_info'
    }

    def __init__(self, xcustomer_id=None, xcustomer_name=None, status=None, judgement=None, incident_id=None, business_type_name=None, incident_type_name=None, customer_id=None, dc_name=None, simple_description=None, source_name=None, create_time=None, message_list=None, incident_satisfaction=None, severity_name=None, business_ownership=None, resolve_time=None, ext_info=None):
        """IncidentDetailInfoV2

        The model defined in huaweicloud sdk

        :param xcustomer_id: 子用户id
        :type xcustomer_id: str
        :param xcustomer_name: 子用户名称
        :type xcustomer_name: str
        :param status: 状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈
        :type status: int
        :param judgement: 评价内容
        :type judgement: str
        :param incident_id: 工单id
        :type incident_id: str
        :param business_type_name: 问题类型名称
        :type business_type_name: str
        :param incident_type_name: 工单类型名称
        :type incident_type_name: str
        :param customer_id: 客户id
        :type customer_id: str
        :param dc_name: 区域名称
        :type dc_name: str
        :param simple_description: 简要描述
        :type simple_description: str
        :param source_name: 来源名称
        :type source_name: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param message_list: 留言列表
        :type message_list: list[:class:`huaweicloudsdkosm.v2.IncidentMessageV2`]
        :param incident_satisfaction: 满意度列表
        :type incident_satisfaction: list[:class:`huaweicloudsdkosm.v2.IncidentSatisfactionV2Do`]
        :param severity_name: 严重性名称
        :type severity_name: str
        :param business_ownership: 业务归属 0华为云 1BP伙伴 2ISV
        :type business_ownership: int
        :param resolve_time: 解决时间
        :type resolve_time: int
        :param ext_info: 
        :type ext_info: :class:`huaweicloudsdkosm.v2.IncidentDetailExtInfoV2`
        """
        
        

        self._xcustomer_id = None
        self._xcustomer_name = None
        self._status = None
        self._judgement = None
        self._incident_id = None
        self._business_type_name = None
        self._incident_type_name = None
        self._customer_id = None
        self._dc_name = None
        self._simple_description = None
        self._source_name = None
        self._create_time = None
        self._message_list = None
        self._incident_satisfaction = None
        self._severity_name = None
        self._business_ownership = None
        self._resolve_time = None
        self._ext_info = None
        self.discriminator = None

        if xcustomer_id is not None:
            self.xcustomer_id = xcustomer_id
        if xcustomer_name is not None:
            self.xcustomer_name = xcustomer_name
        self.status = status
        self.judgement = judgement
        if incident_id is not None:
            self.incident_id = incident_id
        self.business_type_name = business_type_name
        self.incident_type_name = incident_type_name
        self.customer_id = customer_id
        self.dc_name = dc_name
        self.simple_description = simple_description
        self.source_name = source_name
        self.create_time = create_time
        self.message_list = message_list
        self.incident_satisfaction = incident_satisfaction
        if severity_name is not None:
            self.severity_name = severity_name
        if business_ownership is not None:
            self.business_ownership = business_ownership
        if resolve_time is not None:
            self.resolve_time = resolve_time
        if ext_info is not None:
            self.ext_info = ext_info

    @property
    def xcustomer_id(self):
        """Gets the xcustomer_id of this IncidentDetailInfoV2.

        子用户id

        :return: The xcustomer_id of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._xcustomer_id

    @xcustomer_id.setter
    def xcustomer_id(self, xcustomer_id):
        """Sets the xcustomer_id of this IncidentDetailInfoV2.

        子用户id

        :param xcustomer_id: The xcustomer_id of this IncidentDetailInfoV2.
        :type xcustomer_id: str
        """
        self._xcustomer_id = xcustomer_id

    @property
    def xcustomer_name(self):
        """Gets the xcustomer_name of this IncidentDetailInfoV2.

        子用户名称

        :return: The xcustomer_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._xcustomer_name

    @xcustomer_name.setter
    def xcustomer_name(self, xcustomer_name):
        """Sets the xcustomer_name of this IncidentDetailInfoV2.

        子用户名称

        :param xcustomer_name: The xcustomer_name of this IncidentDetailInfoV2.
        :type xcustomer_name: str
        """
        self._xcustomer_name = xcustomer_name

    @property
    def status(self):
        """Gets the status of this IncidentDetailInfoV2.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this IncidentDetailInfoV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentDetailInfoV2.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this IncidentDetailInfoV2.
        :type status: int
        """
        self._status = status

    @property
    def judgement(self):
        """Gets the judgement of this IncidentDetailInfoV2.

        评价内容

        :return: The judgement of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._judgement

    @judgement.setter
    def judgement(self, judgement):
        """Sets the judgement of this IncidentDetailInfoV2.

        评价内容

        :param judgement: The judgement of this IncidentDetailInfoV2.
        :type judgement: str
        """
        self._judgement = judgement

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentDetailInfoV2.

        工单id

        :return: The incident_id of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentDetailInfoV2.

        工单id

        :param incident_id: The incident_id of this IncidentDetailInfoV2.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def business_type_name(self):
        """Gets the business_type_name of this IncidentDetailInfoV2.

        问题类型名称

        :return: The business_type_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._business_type_name

    @business_type_name.setter
    def business_type_name(self, business_type_name):
        """Sets the business_type_name of this IncidentDetailInfoV2.

        问题类型名称

        :param business_type_name: The business_type_name of this IncidentDetailInfoV2.
        :type business_type_name: str
        """
        self._business_type_name = business_type_name

    @property
    def incident_type_name(self):
        """Gets the incident_type_name of this IncidentDetailInfoV2.

        工单类型名称

        :return: The incident_type_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._incident_type_name

    @incident_type_name.setter
    def incident_type_name(self, incident_type_name):
        """Sets the incident_type_name of this IncidentDetailInfoV2.

        工单类型名称

        :param incident_type_name: The incident_type_name of this IncidentDetailInfoV2.
        :type incident_type_name: str
        """
        self._incident_type_name = incident_type_name

    @property
    def customer_id(self):
        """Gets the customer_id of this IncidentDetailInfoV2.

        客户id

        :return: The customer_id of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IncidentDetailInfoV2.

        客户id

        :param customer_id: The customer_id of this IncidentDetailInfoV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def dc_name(self):
        """Gets the dc_name of this IncidentDetailInfoV2.

        区域名称

        :return: The dc_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """Sets the dc_name of this IncidentDetailInfoV2.

        区域名称

        :param dc_name: The dc_name of this IncidentDetailInfoV2.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def simple_description(self):
        """Gets the simple_description of this IncidentDetailInfoV2.

        简要描述

        :return: The simple_description of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this IncidentDetailInfoV2.

        简要描述

        :param simple_description: The simple_description of this IncidentDetailInfoV2.
        :type simple_description: str
        """
        self._simple_description = simple_description

    @property
    def source_name(self):
        """Gets the source_name of this IncidentDetailInfoV2.

        来源名称

        :return: The source_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this IncidentDetailInfoV2.

        来源名称

        :param source_name: The source_name of this IncidentDetailInfoV2.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def create_time(self):
        """Gets the create_time of this IncidentDetailInfoV2.

        创建时间

        :return: The create_time of this IncidentDetailInfoV2.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IncidentDetailInfoV2.

        创建时间

        :param create_time: The create_time of this IncidentDetailInfoV2.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def message_list(self):
        """Gets the message_list of this IncidentDetailInfoV2.

        留言列表

        :return: The message_list of this IncidentDetailInfoV2.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentMessageV2`]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        """Sets the message_list of this IncidentDetailInfoV2.

        留言列表

        :param message_list: The message_list of this IncidentDetailInfoV2.
        :type message_list: list[:class:`huaweicloudsdkosm.v2.IncidentMessageV2`]
        """
        self._message_list = message_list

    @property
    def incident_satisfaction(self):
        """Gets the incident_satisfaction of this IncidentDetailInfoV2.

        满意度列表

        :return: The incident_satisfaction of this IncidentDetailInfoV2.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentSatisfactionV2Do`]
        """
        return self._incident_satisfaction

    @incident_satisfaction.setter
    def incident_satisfaction(self, incident_satisfaction):
        """Sets the incident_satisfaction of this IncidentDetailInfoV2.

        满意度列表

        :param incident_satisfaction: The incident_satisfaction of this IncidentDetailInfoV2.
        :type incident_satisfaction: list[:class:`huaweicloudsdkosm.v2.IncidentSatisfactionV2Do`]
        """
        self._incident_satisfaction = incident_satisfaction

    @property
    def severity_name(self):
        """Gets the severity_name of this IncidentDetailInfoV2.

        严重性名称

        :return: The severity_name of this IncidentDetailInfoV2.
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        """Sets the severity_name of this IncidentDetailInfoV2.

        严重性名称

        :param severity_name: The severity_name of this IncidentDetailInfoV2.
        :type severity_name: str
        """
        self._severity_name = severity_name

    @property
    def business_ownership(self):
        """Gets the business_ownership of this IncidentDetailInfoV2.

        业务归属 0华为云 1BP伙伴 2ISV

        :return: The business_ownership of this IncidentDetailInfoV2.
        :rtype: int
        """
        return self._business_ownership

    @business_ownership.setter
    def business_ownership(self, business_ownership):
        """Sets the business_ownership of this IncidentDetailInfoV2.

        业务归属 0华为云 1BP伙伴 2ISV

        :param business_ownership: The business_ownership of this IncidentDetailInfoV2.
        :type business_ownership: int
        """
        self._business_ownership = business_ownership

    @property
    def resolve_time(self):
        """Gets the resolve_time of this IncidentDetailInfoV2.

        解决时间

        :return: The resolve_time of this IncidentDetailInfoV2.
        :rtype: int
        """
        return self._resolve_time

    @resolve_time.setter
    def resolve_time(self, resolve_time):
        """Sets the resolve_time of this IncidentDetailInfoV2.

        解决时间

        :param resolve_time: The resolve_time of this IncidentDetailInfoV2.
        :type resolve_time: int
        """
        self._resolve_time = resolve_time

    @property
    def ext_info(self):
        """Gets the ext_info of this IncidentDetailInfoV2.

        :return: The ext_info of this IncidentDetailInfoV2.
        :rtype: :class:`huaweicloudsdkosm.v2.IncidentDetailExtInfoV2`
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this IncidentDetailInfoV2.

        :param ext_info: The ext_info of this IncidentDetailInfoV2.
        :type ext_info: :class:`huaweicloudsdkosm.v2.IncidentDetailExtInfoV2`
        """
        self._ext_info = ext_info

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
        if not isinstance(other, IncidentDetailInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
