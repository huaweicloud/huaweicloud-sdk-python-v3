# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_id': 'str',
        'type': 'int',
        'business_type_name': 'str',
        'incident_type_name': 'str',
        'customer_id': 'str',
        'xcustomer_id': 'str',
        'xcustomer_name': 'str',
        'dc_name': 'str',
        'simple_describe': 'str',
        'status': 'int',
        'create_time': 'datetime',
        'gray': 'bool',
        'label_list': 'list[CaseQueryLabel]'
    }

    attribute_map = {
        'incident_id': 'incidentId',
        'type': 'type',
        'business_type_name': 'businessTypeName',
        'incident_type_name': 'incidentTypeName',
        'customer_id': 'customerId',
        'xcustomer_id': 'xcustomerId',
        'xcustomer_name': 'xcustomerName',
        'dc_name': 'dcName',
        'simple_describe': 'simpleDescribe',
        'status': 'status',
        'create_time': 'createTime',
        'gray': 'gray',
        'label_list': 'labelList'
    }

    def __init__(self, incident_id=None, type=None, business_type_name=None, incident_type_name=None, customer_id=None, xcustomer_id=None, xcustomer_name=None, dc_name=None, simple_describe=None, status=None, create_time=None, gray=None, label_list=None):
        r"""IncidentInfo

        The model defined in huaweicloud sdk

        :param incident_id: 工单id
        :type incident_id: str
        :param type: 类型
        :type type: int
        :param business_type_name: 业务分类名称
        :type business_type_name: str
        :param incident_type_name: 工单类型名称
        :type incident_type_name: str
        :param customer_id: 客户id
        :type customer_id: str
        :param xcustomer_id: 客户id
        :type xcustomer_id: str
        :param xcustomer_name: 客户名称
        :type xcustomer_name: str
        :param dc_name: dc名称
        :type dc_name: str
        :param simple_describe: 简单说明
        :type simple_describe: str
        :param status: 工单状态
        :type status: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param gray: 是否灰度
        :type gray: bool
        :param label_list: 标签列表
        :type label_list: list[:class:`huaweicloudsdkosm.v2.CaseQueryLabel`]
        """
        
        

        self._incident_id = None
        self._type = None
        self._business_type_name = None
        self._incident_type_name = None
        self._customer_id = None
        self._xcustomer_id = None
        self._xcustomer_name = None
        self._dc_name = None
        self._simple_describe = None
        self._status = None
        self._create_time = None
        self._gray = None
        self._label_list = None
        self.discriminator = None

        if incident_id is not None:
            self.incident_id = incident_id
        if type is not None:
            self.type = type
        if business_type_name is not None:
            self.business_type_name = business_type_name
        if incident_type_name is not None:
            self.incident_type_name = incident_type_name
        if customer_id is not None:
            self.customer_id = customer_id
        if xcustomer_id is not None:
            self.xcustomer_id = xcustomer_id
        if xcustomer_name is not None:
            self.xcustomer_name = xcustomer_name
        if dc_name is not None:
            self.dc_name = dc_name
        if simple_describe is not None:
            self.simple_describe = simple_describe
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if gray is not None:
            self.gray = gray
        if label_list is not None:
            self.label_list = label_list

    @property
    def incident_id(self):
        r"""Gets the incident_id of this IncidentInfo.

        工单id

        :return: The incident_id of this IncidentInfo.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        r"""Sets the incident_id of this IncidentInfo.

        工单id

        :param incident_id: The incident_id of this IncidentInfo.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def type(self):
        r"""Gets the type of this IncidentInfo.

        类型

        :return: The type of this IncidentInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IncidentInfo.

        类型

        :param type: The type of this IncidentInfo.
        :type type: int
        """
        self._type = type

    @property
    def business_type_name(self):
        r"""Gets the business_type_name of this IncidentInfo.

        业务分类名称

        :return: The business_type_name of this IncidentInfo.
        :rtype: str
        """
        return self._business_type_name

    @business_type_name.setter
    def business_type_name(self, business_type_name):
        r"""Sets the business_type_name of this IncidentInfo.

        业务分类名称

        :param business_type_name: The business_type_name of this IncidentInfo.
        :type business_type_name: str
        """
        self._business_type_name = business_type_name

    @property
    def incident_type_name(self):
        r"""Gets the incident_type_name of this IncidentInfo.

        工单类型名称

        :return: The incident_type_name of this IncidentInfo.
        :rtype: str
        """
        return self._incident_type_name

    @incident_type_name.setter
    def incident_type_name(self, incident_type_name):
        r"""Sets the incident_type_name of this IncidentInfo.

        工单类型名称

        :param incident_type_name: The incident_type_name of this IncidentInfo.
        :type incident_type_name: str
        """
        self._incident_type_name = incident_type_name

    @property
    def customer_id(self):
        r"""Gets the customer_id of this IncidentInfo.

        客户id

        :return: The customer_id of this IncidentInfo.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this IncidentInfo.

        客户id

        :param customer_id: The customer_id of this IncidentInfo.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def xcustomer_id(self):
        r"""Gets the xcustomer_id of this IncidentInfo.

        客户id

        :return: The xcustomer_id of this IncidentInfo.
        :rtype: str
        """
        return self._xcustomer_id

    @xcustomer_id.setter
    def xcustomer_id(self, xcustomer_id):
        r"""Sets the xcustomer_id of this IncidentInfo.

        客户id

        :param xcustomer_id: The xcustomer_id of this IncidentInfo.
        :type xcustomer_id: str
        """
        self._xcustomer_id = xcustomer_id

    @property
    def xcustomer_name(self):
        r"""Gets the xcustomer_name of this IncidentInfo.

        客户名称

        :return: The xcustomer_name of this IncidentInfo.
        :rtype: str
        """
        return self._xcustomer_name

    @xcustomer_name.setter
    def xcustomer_name(self, xcustomer_name):
        r"""Sets the xcustomer_name of this IncidentInfo.

        客户名称

        :param xcustomer_name: The xcustomer_name of this IncidentInfo.
        :type xcustomer_name: str
        """
        self._xcustomer_name = xcustomer_name

    @property
    def dc_name(self):
        r"""Gets the dc_name of this IncidentInfo.

        dc名称

        :return: The dc_name of this IncidentInfo.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        r"""Sets the dc_name of this IncidentInfo.

        dc名称

        :param dc_name: The dc_name of this IncidentInfo.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def simple_describe(self):
        r"""Gets the simple_describe of this IncidentInfo.

        简单说明

        :return: The simple_describe of this IncidentInfo.
        :rtype: str
        """
        return self._simple_describe

    @simple_describe.setter
    def simple_describe(self, simple_describe):
        r"""Sets the simple_describe of this IncidentInfo.

        简单说明

        :param simple_describe: The simple_describe of this IncidentInfo.
        :type simple_describe: str
        """
        self._simple_describe = simple_describe

    @property
    def status(self):
        r"""Gets the status of this IncidentInfo.

        工单状态

        :return: The status of this IncidentInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IncidentInfo.

        工单状态

        :param status: The status of this IncidentInfo.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this IncidentInfo.

        创建时间

        :return: The create_time of this IncidentInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this IncidentInfo.

        创建时间

        :param create_time: The create_time of this IncidentInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def gray(self):
        r"""Gets the gray of this IncidentInfo.

        是否灰度

        :return: The gray of this IncidentInfo.
        :rtype: bool
        """
        return self._gray

    @gray.setter
    def gray(self, gray):
        r"""Sets the gray of this IncidentInfo.

        是否灰度

        :param gray: The gray of this IncidentInfo.
        :type gray: bool
        """
        self._gray = gray

    @property
    def label_list(self):
        r"""Gets the label_list of this IncidentInfo.

        标签列表

        :return: The label_list of this IncidentInfo.
        :rtype: list[:class:`huaweicloudsdkosm.v2.CaseQueryLabel`]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this IncidentInfo.

        标签列表

        :param label_list: The label_list of this IncidentInfo.
        :type label_list: list[:class:`huaweicloudsdkosm.v2.CaseQueryLabel`]
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
        if not isinstance(other, IncidentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
