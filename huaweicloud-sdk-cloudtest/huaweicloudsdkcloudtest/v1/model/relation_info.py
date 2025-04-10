# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dr_number': 'str',
        'test_case_uri': 'str',
        'relate_type': 'str',
        'resource_type': 'str',
        'source_system': 'str',
        'association_number': 'str',
        'region': 'str'
    }

    attribute_map = {
        'dr_number': 'dr_number',
        'test_case_uri': 'test_case_uri',
        'relate_type': 'relate_type',
        'resource_type': 'resource_type',
        'source_system': 'source_system',
        'association_number': 'association_number',
        'region': 'region'
    }

    def __init__(self, dr_number=None, test_case_uri=None, relate_type=None, resource_type=None, source_system=None, association_number=None, region=None):
        r"""RelationInfo

        The model defined in huaweicloud sdk

        :param dr_number: 需求id
        :type dr_number: str
        :param test_case_uri: 用例uri
        :type test_case_uri: str
        :param relate_type: 资源类型
        :type relate_type: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param source_system: 来源系统
        :type source_system: str
        :param association_number: 关联资源编号
        :type association_number: str
        :param region: 逻辑region，外部使用公有云实际区域，内部使用默认值
        :type region: str
        """
        
        

        self._dr_number = None
        self._test_case_uri = None
        self._relate_type = None
        self._resource_type = None
        self._source_system = None
        self._association_number = None
        self._region = None
        self.discriminator = None

        self.dr_number = dr_number
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        self.relate_type = relate_type
        if resource_type is not None:
            self.resource_type = resource_type
        if source_system is not None:
            self.source_system = source_system
        if association_number is not None:
            self.association_number = association_number
        if region is not None:
            self.region = region

    @property
    def dr_number(self):
        r"""Gets the dr_number of this RelationInfo.

        需求id

        :return: The dr_number of this RelationInfo.
        :rtype: str
        """
        return self._dr_number

    @dr_number.setter
    def dr_number(self, dr_number):
        r"""Sets the dr_number of this RelationInfo.

        需求id

        :param dr_number: The dr_number of this RelationInfo.
        :type dr_number: str
        """
        self._dr_number = dr_number

    @property
    def test_case_uri(self):
        r"""Gets the test_case_uri of this RelationInfo.

        用例uri

        :return: The test_case_uri of this RelationInfo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        r"""Sets the test_case_uri of this RelationInfo.

        用例uri

        :param test_case_uri: The test_case_uri of this RelationInfo.
        :type test_case_uri: str
        """
        self._test_case_uri = test_case_uri

    @property
    def relate_type(self):
        r"""Gets the relate_type of this RelationInfo.

        资源类型

        :return: The relate_type of this RelationInfo.
        :rtype: str
        """
        return self._relate_type

    @relate_type.setter
    def relate_type(self, relate_type):
        r"""Sets the relate_type of this RelationInfo.

        资源类型

        :param relate_type: The relate_type of this RelationInfo.
        :type relate_type: str
        """
        self._relate_type = relate_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this RelationInfo.

        资源类型

        :return: The resource_type of this RelationInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this RelationInfo.

        资源类型

        :param resource_type: The resource_type of this RelationInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def source_system(self):
        r"""Gets the source_system of this RelationInfo.

        来源系统

        :return: The source_system of this RelationInfo.
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        r"""Sets the source_system of this RelationInfo.

        来源系统

        :param source_system: The source_system of this RelationInfo.
        :type source_system: str
        """
        self._source_system = source_system

    @property
    def association_number(self):
        r"""Gets the association_number of this RelationInfo.

        关联资源编号

        :return: The association_number of this RelationInfo.
        :rtype: str
        """
        return self._association_number

    @association_number.setter
    def association_number(self, association_number):
        r"""Sets the association_number of this RelationInfo.

        关联资源编号

        :param association_number: The association_number of this RelationInfo.
        :type association_number: str
        """
        self._association_number = association_number

    @property
    def region(self):
        r"""Gets the region of this RelationInfo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :return: The region of this RelationInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RelationInfo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :param region: The region of this RelationInfo.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, RelationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
