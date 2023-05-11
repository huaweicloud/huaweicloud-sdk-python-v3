# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonthlyExpendituresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cycle': 'str',
        'cloud_service_type_code': 'str',
        'type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'cycle': 'cycle',
        'cloud_service_type_code': 'cloud_service_type_code',
        'type': 'type',
        'enterprise_project_id': 'enterpriseProjectId'
    }

    def __init__(self, cycle=None, cloud_service_type_code=None, type=None, enterprise_project_id=None):
        """ListMonthlyExpendituresRequest

        The model defined in huaweicloud sdk

        :param cycle: 查询消费汇总账单所在的账期，格式为YYYY-MM。
        :type cycle: str
        :param cloud_service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。当不传递此参数时，查询的账单是以云服务类型为维度的月度消费账单。当传递此参数时，查询的账单是该云服务类型下以资源类型为维度的月度消费账单。
        :type cloud_service_type_code: str
        :param type: 0：华为云账户 1：伙伴设置预算账户，仅当客户关联合作伙伴且关联类型为转售模式时，才会存在伙伴拨款设置预算账户。不传此参数默认查询华为云账户下的消费汇总。
        :type type: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._cycle = None
        self._cloud_service_type_code = None
        self._type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.cycle = cycle
        if cloud_service_type_code is not None:
            self.cloud_service_type_code = cloud_service_type_code
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def cycle(self):
        """Gets the cycle of this ListMonthlyExpendituresRequest.

        查询消费汇总账单所在的账期，格式为YYYY-MM。

        :return: The cycle of this ListMonthlyExpendituresRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListMonthlyExpendituresRequest.

        查询消费汇总账单所在的账期，格式为YYYY-MM。

        :param cycle: The cycle of this ListMonthlyExpendituresRequest.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type_code(self):
        """Gets the cloud_service_type_code of this ListMonthlyExpendituresRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。当不传递此参数时，查询的账单是以云服务类型为维度的月度消费账单。当传递此参数时，查询的账单是该云服务类型下以资源类型为维度的月度消费账单。

        :return: The cloud_service_type_code of this ListMonthlyExpendituresRequest.
        :rtype: str
        """
        return self._cloud_service_type_code

    @cloud_service_type_code.setter
    def cloud_service_type_code(self, cloud_service_type_code):
        """Sets the cloud_service_type_code of this ListMonthlyExpendituresRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。当不传递此参数时，查询的账单是以云服务类型为维度的月度消费账单。当传递此参数时，查询的账单是该云服务类型下以资源类型为维度的月度消费账单。

        :param cloud_service_type_code: The cloud_service_type_code of this ListMonthlyExpendituresRequest.
        :type cloud_service_type_code: str
        """
        self._cloud_service_type_code = cloud_service_type_code

    @property
    def type(self):
        """Gets the type of this ListMonthlyExpendituresRequest.

        0：华为云账户 1：伙伴设置预算账户，仅当客户关联合作伙伴且关联类型为转售模式时，才会存在伙伴拨款设置预算账户。不传此参数默认查询华为云账户下的消费汇总。

        :return: The type of this ListMonthlyExpendituresRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListMonthlyExpendituresRequest.

        0：华为云账户 1：伙伴设置预算账户，仅当客户关联合作伙伴且关联类型为转售模式时，才会存在伙伴拨款设置预算账户。不传此参数默认查询华为云账户下的消费汇总。

        :param type: The type of this ListMonthlyExpendituresRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListMonthlyExpendituresRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListMonthlyExpendituresRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListMonthlyExpendituresRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListMonthlyExpendituresRequest.
        :type enterprise_project_id: str
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
        if not isinstance(other, ListMonthlyExpendituresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
