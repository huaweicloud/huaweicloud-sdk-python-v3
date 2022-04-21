# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentInfoV2:

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
        'incident_id': 'str',
        'business_type_name': 'str',
        'incident_type_name': 'str',
        'customer_id': 'str',
        'dc_name': 'str',
        'simple_description': 'str',
        'create_time': 'datetime',
        'label_list': 'list[LabelInfo]'
    }

    attribute_map = {
        'xcustomer_id': 'xcustomer_id',
        'xcustomer_name': 'xcustomer_name',
        'status': 'status',
        'incident_id': 'incident_id',
        'business_type_name': 'business_type_name',
        'incident_type_name': 'incident_type_name',
        'customer_id': 'customer_id',
        'dc_name': 'dc_name',
        'simple_description': 'simple_description',
        'create_time': 'create_time',
        'label_list': 'label_list'
    }

    def __init__(self, xcustomer_id=None, xcustomer_name=None, status=None, incident_id=None, business_type_name=None, incident_type_name=None, customer_id=None, dc_name=None, simple_description=None, create_time=None, label_list=None):
        """IncidentInfoV2

        The model defined in huaweicloud sdk

        :param xcustomer_id: 子用户id
        :type xcustomer_id: str
        :param xcustomer_name: 子用户名称
        :type xcustomer_name: str
        :param status: 状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈
        :type status: int
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
        :param create_time: 创建时间
        :type create_time: datetime
        :param label_list: 标签列表
        :type label_list: list[:class:`huaweicloudsdkosm.v2.LabelInfo`]
        """
        
        

        self._xcustomer_id = None
        self._xcustomer_name = None
        self._status = None
        self._incident_id = None
        self._business_type_name = None
        self._incident_type_name = None
        self._customer_id = None
        self._dc_name = None
        self._simple_description = None
        self._create_time = None
        self._label_list = None
        self.discriminator = None

        if xcustomer_id is not None:
            self.xcustomer_id = xcustomer_id
        if xcustomer_name is not None:
            self.xcustomer_name = xcustomer_name
        self.status = status
        self.incident_id = incident_id
        self.business_type_name = business_type_name
        self.incident_type_name = incident_type_name
        self.customer_id = customer_id
        self.dc_name = dc_name
        self.simple_description = simple_description
        self.create_time = create_time
        if label_list is not None:
            self.label_list = label_list

    @property
    def xcustomer_id(self):
        """Gets the xcustomer_id of this IncidentInfoV2.

        子用户id

        :return: The xcustomer_id of this IncidentInfoV2.
        :rtype: str
        """
        return self._xcustomer_id

    @xcustomer_id.setter
    def xcustomer_id(self, xcustomer_id):
        """Sets the xcustomer_id of this IncidentInfoV2.

        子用户id

        :param xcustomer_id: The xcustomer_id of this IncidentInfoV2.
        :type xcustomer_id: str
        """
        self._xcustomer_id = xcustomer_id

    @property
    def xcustomer_name(self):
        """Gets the xcustomer_name of this IncidentInfoV2.

        子用户名称

        :return: The xcustomer_name of this IncidentInfoV2.
        :rtype: str
        """
        return self._xcustomer_name

    @xcustomer_name.setter
    def xcustomer_name(self, xcustomer_name):
        """Sets the xcustomer_name of this IncidentInfoV2.

        子用户名称

        :param xcustomer_name: The xcustomer_name of this IncidentInfoV2.
        :type xcustomer_name: str
        """
        self._xcustomer_name = xcustomer_name

    @property
    def status(self):
        """Gets the status of this IncidentInfoV2.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this IncidentInfoV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentInfoV2.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this IncidentInfoV2.
        :type status: int
        """
        self._status = status

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentInfoV2.

        工单id

        :return: The incident_id of this IncidentInfoV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentInfoV2.

        工单id

        :param incident_id: The incident_id of this IncidentInfoV2.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def business_type_name(self):
        """Gets the business_type_name of this IncidentInfoV2.

        问题类型名称

        :return: The business_type_name of this IncidentInfoV2.
        :rtype: str
        """
        return self._business_type_name

    @business_type_name.setter
    def business_type_name(self, business_type_name):
        """Sets the business_type_name of this IncidentInfoV2.

        问题类型名称

        :param business_type_name: The business_type_name of this IncidentInfoV2.
        :type business_type_name: str
        """
        self._business_type_name = business_type_name

    @property
    def incident_type_name(self):
        """Gets the incident_type_name of this IncidentInfoV2.

        工单类型名称

        :return: The incident_type_name of this IncidentInfoV2.
        :rtype: str
        """
        return self._incident_type_name

    @incident_type_name.setter
    def incident_type_name(self, incident_type_name):
        """Sets the incident_type_name of this IncidentInfoV2.

        工单类型名称

        :param incident_type_name: The incident_type_name of this IncidentInfoV2.
        :type incident_type_name: str
        """
        self._incident_type_name = incident_type_name

    @property
    def customer_id(self):
        """Gets the customer_id of this IncidentInfoV2.

        客户id

        :return: The customer_id of this IncidentInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IncidentInfoV2.

        客户id

        :param customer_id: The customer_id of this IncidentInfoV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def dc_name(self):
        """Gets the dc_name of this IncidentInfoV2.

        区域名称

        :return: The dc_name of this IncidentInfoV2.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """Sets the dc_name of this IncidentInfoV2.

        区域名称

        :param dc_name: The dc_name of this IncidentInfoV2.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def simple_description(self):
        """Gets the simple_description of this IncidentInfoV2.

        简要描述

        :return: The simple_description of this IncidentInfoV2.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this IncidentInfoV2.

        简要描述

        :param simple_description: The simple_description of this IncidentInfoV2.
        :type simple_description: str
        """
        self._simple_description = simple_description

    @property
    def create_time(self):
        """Gets the create_time of this IncidentInfoV2.

        创建时间

        :return: The create_time of this IncidentInfoV2.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IncidentInfoV2.

        创建时间

        :param create_time: The create_time of this IncidentInfoV2.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def label_list(self):
        """Gets the label_list of this IncidentInfoV2.

        标签列表

        :return: The label_list of this IncidentInfoV2.
        :rtype: list[:class:`huaweicloudsdkosm.v2.LabelInfo`]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this IncidentInfoV2.

        标签列表

        :param label_list: The label_list of this IncidentInfoV2.
        :type label_list: list[:class:`huaweicloudsdkosm.v2.LabelInfo`]
        """
        self._label_list = label_list

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
        if not isinstance(other, IncidentInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
