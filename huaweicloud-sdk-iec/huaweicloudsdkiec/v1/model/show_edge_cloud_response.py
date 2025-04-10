# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeCloudResponse(SdkResponse):

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
        'stacks': 'list[Stack]',
        'coverage': 'CoverageResp',
        'success_num': 'int',
        'failed_num': 'int',
        'status': 'str',
        'fail_reason': 'FailReason',
        'edge_regions': 'int',
        'description': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stacks': 'stacks',
        'coverage': 'coverage',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'status': 'status',
        'fail_reason': 'fail_reason',
        'edge_regions': 'edge_regions',
        'description': 'description',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, name=None, stacks=None, coverage=None, success_num=None, failed_num=None, status=None, fail_reason=None, edge_regions=None, description=None, create_at=None, update_at=None):
        r"""ShowEdgeCloudResponse

        The model defined in huaweicloud sdk

        :param id: 边缘业务ID。
        :type id: str
        :param name: 边缘业务名称。
        :type name: str
        :param stacks: 边缘业务资源组。
        :type stacks: list[:class:`huaweicloudsdkiec.v1.Stack`]
        :param coverage: 
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageResp`
        :param success_num: 边缘业务成功创建的虚拟机数量。
        :type success_num: int
        :param failed_num: 边缘业务创建失败的虚拟机数量。
        :type failed_num: int
        :param status: 边缘业务状态。
        :type status: str
        :param fail_reason: 
        :type fail_reason: :class:`huaweicloudsdkiec.v1.FailReason`
        :param edge_regions: 边缘业务支持的边缘区域数目，等同于边缘业务下所有实例的区域数目总和
        :type edge_regions: int
        :param description: 描述。
        :type description: str
        :param create_at: 创建时间。
        :type create_at: str
        :param update_at: 修改时间。
        :type update_at: str
        """
        
        super(ShowEdgeCloudResponse, self).__init__()

        self._id = None
        self._name = None
        self._stacks = None
        self._coverage = None
        self._success_num = None
        self._failed_num = None
        self._status = None
        self._fail_reason = None
        self._edge_regions = None
        self._description = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if stacks is not None:
            self.stacks = stacks
        if coverage is not None:
            self.coverage = coverage
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if edge_regions is not None:
            self.edge_regions = edge_regions
        if description is not None:
            self.description = description
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this ShowEdgeCloudResponse.

        边缘业务ID。

        :return: The id of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowEdgeCloudResponse.

        边缘业务ID。

        :param id: The id of this ShowEdgeCloudResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowEdgeCloudResponse.

        边缘业务名称。

        :return: The name of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowEdgeCloudResponse.

        边缘业务名称。

        :param name: The name of this ShowEdgeCloudResponse.
        :type name: str
        """
        self._name = name

    @property
    def stacks(self):
        r"""Gets the stacks of this ShowEdgeCloudResponse.

        边缘业务资源组。

        :return: The stacks of this ShowEdgeCloudResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Stack`]
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        r"""Sets the stacks of this ShowEdgeCloudResponse.

        边缘业务资源组。

        :param stacks: The stacks of this ShowEdgeCloudResponse.
        :type stacks: list[:class:`huaweicloudsdkiec.v1.Stack`]
        """
        self._stacks = stacks

    @property
    def coverage(self):
        r"""Gets the coverage of this ShowEdgeCloudResponse.

        :return: The coverage of this ShowEdgeCloudResponse.
        :rtype: :class:`huaweicloudsdkiec.v1.CoverageResp`
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        r"""Sets the coverage of this ShowEdgeCloudResponse.

        :param coverage: The coverage of this ShowEdgeCloudResponse.
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageResp`
        """
        self._coverage = coverage

    @property
    def success_num(self):
        r"""Gets the success_num of this ShowEdgeCloudResponse.

        边缘业务成功创建的虚拟机数量。

        :return: The success_num of this ShowEdgeCloudResponse.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ShowEdgeCloudResponse.

        边缘业务成功创建的虚拟机数量。

        :param success_num: The success_num of this ShowEdgeCloudResponse.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this ShowEdgeCloudResponse.

        边缘业务创建失败的虚拟机数量。

        :return: The failed_num of this ShowEdgeCloudResponse.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this ShowEdgeCloudResponse.

        边缘业务创建失败的虚拟机数量。

        :param failed_num: The failed_num of this ShowEdgeCloudResponse.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def status(self):
        r"""Gets the status of this ShowEdgeCloudResponse.

        边缘业务状态。

        :return: The status of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowEdgeCloudResponse.

        边缘业务状态。

        :param status: The status of this ShowEdgeCloudResponse.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ShowEdgeCloudResponse.

        :return: The fail_reason of this ShowEdgeCloudResponse.
        :rtype: :class:`huaweicloudsdkiec.v1.FailReason`
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ShowEdgeCloudResponse.

        :param fail_reason: The fail_reason of this ShowEdgeCloudResponse.
        :type fail_reason: :class:`huaweicloudsdkiec.v1.FailReason`
        """
        self._fail_reason = fail_reason

    @property
    def edge_regions(self):
        r"""Gets the edge_regions of this ShowEdgeCloudResponse.

        边缘业务支持的边缘区域数目，等同于边缘业务下所有实例的区域数目总和

        :return: The edge_regions of this ShowEdgeCloudResponse.
        :rtype: int
        """
        return self._edge_regions

    @edge_regions.setter
    def edge_regions(self, edge_regions):
        r"""Sets the edge_regions of this ShowEdgeCloudResponse.

        边缘业务支持的边缘区域数目，等同于边缘业务下所有实例的区域数目总和

        :param edge_regions: The edge_regions of this ShowEdgeCloudResponse.
        :type edge_regions: int
        """
        self._edge_regions = edge_regions

    @property
    def description(self):
        r"""Gets the description of this ShowEdgeCloudResponse.

        描述。

        :return: The description of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowEdgeCloudResponse.

        描述。

        :param description: The description of this ShowEdgeCloudResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowEdgeCloudResponse.

        创建时间。

        :return: The create_at of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowEdgeCloudResponse.

        创建时间。

        :param create_at: The create_at of this ShowEdgeCloudResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowEdgeCloudResponse.

        修改时间。

        :return: The update_at of this ShowEdgeCloudResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowEdgeCloudResponse.

        修改时间。

        :param update_at: The update_at of this ShowEdgeCloudResponse.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, ShowEdgeCloudResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
