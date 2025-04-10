# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperationVO:

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
        'tenant_id': 'str',
        'group_id': 'str',
        'biz_name': 'str',
        'biz_id': 'str',
        'operation_status': 'str',
        'operation_type': 'str',
        'biz_info': 'str',
        'create_by': 'str',
        'remark': 'str',
        'total': 'int',
        'success': 'int',
        'failed': 'int',
        'rate': 'str',
        'logs': 'str',
        'groups': 'list[BatchOperationVO]'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'group_id': 'group_id',
        'biz_name': 'biz_name',
        'biz_id': 'biz_id',
        'operation_status': 'operation_status',
        'operation_type': 'operation_type',
        'biz_info': 'biz_info',
        'create_by': 'create_by',
        'remark': 'remark',
        'total': 'total',
        'success': 'success',
        'failed': 'failed',
        'rate': 'rate',
        'logs': 'logs',
        'groups': 'groups'
    }

    def __init__(self, id=None, tenant_id=None, group_id=None, biz_name=None, biz_id=None, operation_status=None, operation_type=None, biz_info=None, create_by=None, remark=None, total=None, success=None, failed=None, rate=None, logs=None, groups=None):
        r"""BatchOperationVO

        The model defined in huaweicloud sdk

        :param id: 批量审批ID，ID字符串。
        :type id: str
        :param tenant_id: 项目ID。
        :type tenant_id: str
        :param group_id: 组ID，ID字符串。
        :type group_id: str
        :param biz_name: 业务名。
        :type biz_name: str
        :param biz_id: 业务ID，ID字符串。
        :type biz_id: str
        :param operation_status: 操作结果类型枚举。RUNNING(运行中)、SUCCESS(操作成功)、FAILED(操作失败)。 枚举值：   - RUNNING: 运行中   - SUCCESS: 操作成功   - FAILED: 操作失败 
        :type operation_status: str
        :param operation_type: 类型。
        :type operation_type: str
        :param biz_info: 业务详情。
        :type biz_info: str
        :param create_by: 创建人。
        :type create_by: str
        :param remark: remark信息。
        :type remark: str
        :param total: 总数。
        :type total: int
        :param success: 操作成功个数。
        :type success: int
        :param failed: 操作失败个数。
        :type failed: int
        :param rate: 当前进度。
        :type rate: str
        :param logs: 日志。
        :type logs: str
        :param groups: 分组信息。
        :type groups: list[:class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`]
        """
        
        

        self._id = None
        self._tenant_id = None
        self._group_id = None
        self._biz_name = None
        self._biz_id = None
        self._operation_status = None
        self._operation_type = None
        self._biz_info = None
        self._create_by = None
        self._remark = None
        self._total = None
        self._success = None
        self._failed = None
        self._rate = None
        self._logs = None
        self._groups = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if group_id is not None:
            self.group_id = group_id
        if biz_name is not None:
            self.biz_name = biz_name
        if biz_id is not None:
            self.biz_id = biz_id
        if operation_status is not None:
            self.operation_status = operation_status
        if operation_type is not None:
            self.operation_type = operation_type
        if biz_info is not None:
            self.biz_info = biz_info
        if create_by is not None:
            self.create_by = create_by
        if remark is not None:
            self.remark = remark
        if total is not None:
            self.total = total
        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if rate is not None:
            self.rate = rate
        if logs is not None:
            self.logs = logs
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        r"""Gets the id of this BatchOperationVO.

        批量审批ID，ID字符串。

        :return: The id of this BatchOperationVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchOperationVO.

        批量审批ID，ID字符串。

        :param id: The id of this BatchOperationVO.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this BatchOperationVO.

        项目ID。

        :return: The tenant_id of this BatchOperationVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this BatchOperationVO.

        项目ID。

        :param tenant_id: The tenant_id of this BatchOperationVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def group_id(self):
        r"""Gets the group_id of this BatchOperationVO.

        组ID，ID字符串。

        :return: The group_id of this BatchOperationVO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this BatchOperationVO.

        组ID，ID字符串。

        :param group_id: The group_id of this BatchOperationVO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def biz_name(self):
        r"""Gets the biz_name of this BatchOperationVO.

        业务名。

        :return: The biz_name of this BatchOperationVO.
        :rtype: str
        """
        return self._biz_name

    @biz_name.setter
    def biz_name(self, biz_name):
        r"""Sets the biz_name of this BatchOperationVO.

        业务名。

        :param biz_name: The biz_name of this BatchOperationVO.
        :type biz_name: str
        """
        self._biz_name = biz_name

    @property
    def biz_id(self):
        r"""Gets the biz_id of this BatchOperationVO.

        业务ID，ID字符串。

        :return: The biz_id of this BatchOperationVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this BatchOperationVO.

        业务ID，ID字符串。

        :param biz_id: The biz_id of this BatchOperationVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def operation_status(self):
        r"""Gets the operation_status of this BatchOperationVO.

        操作结果类型枚举。RUNNING(运行中)、SUCCESS(操作成功)、FAILED(操作失败)。 枚举值：   - RUNNING: 运行中   - SUCCESS: 操作成功   - FAILED: 操作失败 

        :return: The operation_status of this BatchOperationVO.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this BatchOperationVO.

        操作结果类型枚举。RUNNING(运行中)、SUCCESS(操作成功)、FAILED(操作失败)。 枚举值：   - RUNNING: 运行中   - SUCCESS: 操作成功   - FAILED: 操作失败 

        :param operation_status: The operation_status of this BatchOperationVO.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def operation_type(self):
        r"""Gets the operation_type of this BatchOperationVO.

        类型。

        :return: The operation_type of this BatchOperationVO.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this BatchOperationVO.

        类型。

        :param operation_type: The operation_type of this BatchOperationVO.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def biz_info(self):
        r"""Gets the biz_info of this BatchOperationVO.

        业务详情。

        :return: The biz_info of this BatchOperationVO.
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        r"""Sets the biz_info of this BatchOperationVO.

        业务详情。

        :param biz_info: The biz_info of this BatchOperationVO.
        :type biz_info: str
        """
        self._biz_info = biz_info

    @property
    def create_by(self):
        r"""Gets the create_by of this BatchOperationVO.

        创建人。

        :return: The create_by of this BatchOperationVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this BatchOperationVO.

        创建人。

        :param create_by: The create_by of this BatchOperationVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def remark(self):
        r"""Gets the remark of this BatchOperationVO.

        remark信息。

        :return: The remark of this BatchOperationVO.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this BatchOperationVO.

        remark信息。

        :param remark: The remark of this BatchOperationVO.
        :type remark: str
        """
        self._remark = remark

    @property
    def total(self):
        r"""Gets the total of this BatchOperationVO.

        总数。

        :return: The total of this BatchOperationVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BatchOperationVO.

        总数。

        :param total: The total of this BatchOperationVO.
        :type total: int
        """
        self._total = total

    @property
    def success(self):
        r"""Gets the success of this BatchOperationVO.

        操作成功个数。

        :return: The success of this BatchOperationVO.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this BatchOperationVO.

        操作成功个数。

        :param success: The success of this BatchOperationVO.
        :type success: int
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this BatchOperationVO.

        操作失败个数。

        :return: The failed of this BatchOperationVO.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this BatchOperationVO.

        操作失败个数。

        :param failed: The failed of this BatchOperationVO.
        :type failed: int
        """
        self._failed = failed

    @property
    def rate(self):
        r"""Gets the rate of this BatchOperationVO.

        当前进度。

        :return: The rate of this BatchOperationVO.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        r"""Sets the rate of this BatchOperationVO.

        当前进度。

        :param rate: The rate of this BatchOperationVO.
        :type rate: str
        """
        self._rate = rate

    @property
    def logs(self):
        r"""Gets the logs of this BatchOperationVO.

        日志。

        :return: The logs of this BatchOperationVO.
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this BatchOperationVO.

        日志。

        :param logs: The logs of this BatchOperationVO.
        :type logs: str
        """
        self._logs = logs

    @property
    def groups(self):
        r"""Gets the groups of this BatchOperationVO.

        分组信息。

        :return: The groups of this BatchOperationVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this BatchOperationVO.

        分组信息。

        :param groups: The groups of this BatchOperationVO.
        :type groups: list[:class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`]
        """
        self._groups = groups

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
        if not isinstance(other, BatchOperationVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
