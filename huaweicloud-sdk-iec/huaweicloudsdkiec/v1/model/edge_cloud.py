# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeCloud:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'coverage': 'CoverageResp',
        'failed_num': 'int',
        'status': 'str',
        'success_num': 'int',
        'edge_regions': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'coverage': 'coverage',
        'failed_num': 'failed_num',
        'status': 'status',
        'success_num': 'success_num',
        'edge_regions': 'edge_regions'
    }

    def __init__(self, id=None, name=None, description=None, coverage=None, failed_num=None, status=None, success_num=None, edge_regions=None):
        """EdgeCloud

        The model defined in huaweicloud sdk

        :param id: 边缘业务ID。
        :type id: str
        :param name: 边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。
        :type name: str
        :param description: 边缘业务描述。最大支持255字节。
        :type description: str
        :param coverage: 
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageResp`
        :param failed_num: 创建失败的虚拟机
        :type failed_num: int
        :param status: 边缘业务状态，现存状态有： - creating/scheduling/updating：部署中 - inService：运行中 - failed：创建失败 - deleting：删除中 - delFailed：删除失败
        :type status: str
        :param success_num: 成功创建的虚拟机
        :type success_num: int
        :param edge_regions: 边缘业务支持的边缘区域数目。
        :type edge_regions: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._coverage = None
        self._failed_num = None
        self._status = None
        self._success_num = None
        self._edge_regions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if coverage is not None:
            self.coverage = coverage
        if failed_num is not None:
            self.failed_num = failed_num
        if status is not None:
            self.status = status
        if success_num is not None:
            self.success_num = success_num
        if edge_regions is not None:
            self.edge_regions = edge_regions

    @property
    def id(self):
        """Gets the id of this EdgeCloud.

        边缘业务ID。

        :return: The id of this EdgeCloud.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeCloud.

        边缘业务ID。

        :param id: The id of this EdgeCloud.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EdgeCloud.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :return: The name of this EdgeCloud.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeCloud.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :param name: The name of this EdgeCloud.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EdgeCloud.

        边缘业务描述。最大支持255字节。

        :return: The description of this EdgeCloud.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeCloud.

        边缘业务描述。最大支持255字节。

        :param description: The description of this EdgeCloud.
        :type description: str
        """
        self._description = description

    @property
    def coverage(self):
        """Gets the coverage of this EdgeCloud.

        :return: The coverage of this EdgeCloud.
        :rtype: :class:`huaweicloudsdkiec.v1.CoverageResp`
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this EdgeCloud.

        :param coverage: The coverage of this EdgeCloud.
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageResp`
        """
        self._coverage = coverage

    @property
    def failed_num(self):
        """Gets the failed_num of this EdgeCloud.

        创建失败的虚拟机

        :return: The failed_num of this EdgeCloud.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this EdgeCloud.

        创建失败的虚拟机

        :param failed_num: The failed_num of this EdgeCloud.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def status(self):
        """Gets the status of this EdgeCloud.

        边缘业务状态，现存状态有： - creating/scheduling/updating：部署中 - inService：运行中 - failed：创建失败 - deleting：删除中 - delFailed：删除失败

        :return: The status of this EdgeCloud.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EdgeCloud.

        边缘业务状态，现存状态有： - creating/scheduling/updating：部署中 - inService：运行中 - failed：创建失败 - deleting：删除中 - delFailed：删除失败

        :param status: The status of this EdgeCloud.
        :type status: str
        """
        self._status = status

    @property
    def success_num(self):
        """Gets the success_num of this EdgeCloud.

        成功创建的虚拟机

        :return: The success_num of this EdgeCloud.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this EdgeCloud.

        成功创建的虚拟机

        :param success_num: The success_num of this EdgeCloud.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def edge_regions(self):
        """Gets the edge_regions of this EdgeCloud.

        边缘业务支持的边缘区域数目。

        :return: The edge_regions of this EdgeCloud.
        :rtype: int
        """
        return self._edge_regions

    @edge_regions.setter
    def edge_regions(self, edge_regions):
        """Sets the edge_regions of this EdgeCloud.

        边缘业务支持的边缘区域数目。

        :param edge_regions: The edge_regions of this EdgeCloud.
        :type edge_regions: int
        """
        self._edge_regions = edge_regions

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
        if not isinstance(other, EdgeCloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
