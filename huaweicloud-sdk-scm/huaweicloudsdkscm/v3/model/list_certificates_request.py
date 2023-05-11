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
        'limit': 'int',
        'offset': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str',
        'enterprise_project_id': 'str',
        'deploy_support': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'deploy_support': 'deploy_support'
    }

    def __init__(self, limit=None, offset=None, sort_dir=None, sort_key=None, status=None, enterprise_project_id=None, deploy_support=None):
        """ListCertificatesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。
        :type limit: int
        :param offset: 偏移量。
        :type offset: int
        :param sort_dir: 排序方式。根据排序参数sort_key进行排序，取值如下： - ASC：升序。 - DESC：降序。
        :type sort_dir: str
        :param sort_key: 排序依据参数，取值如下： - certExpiredTime：证书到期时间。 - certStatus：证书状态。 - certUpdateTime：证书更新时间。
        :type sort_key: str
        :param status: 证书状态，取值如下： - ALL：所有证书状态。 - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - CHECKING_ORG：待完成企业资格认证。 - ISSUING：证书待签发。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。
        :type status: str
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        :param deploy_support: 是否支持部署。
        :type deploy_support: bool
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self._enterprise_project_id = None
        self._deploy_support = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if deploy_support is not None:
            self.deploy_support = deploy_support

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :param limit: The limit of this ListCertificatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListCertificatesRequest.

        偏移量。

        :return: The offset of this ListCertificatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCertificatesRequest.

        偏移量。

        :param offset: The offset of this ListCertificatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListCertificatesRequest.

        排序方式。根据排序参数sort_key进行排序，取值如下： - ASC：升序。 - DESC：降序。

        :return: The sort_dir of this ListCertificatesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListCertificatesRequest.

        排序方式。根据排序参数sort_key进行排序，取值如下： - ASC：升序。 - DESC：降序。

        :param sort_dir: The sort_dir of this ListCertificatesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListCertificatesRequest.

        排序依据参数，取值如下： - certExpiredTime：证书到期时间。 - certStatus：证书状态。 - certUpdateTime：证书更新时间。

        :return: The sort_key of this ListCertificatesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListCertificatesRequest.

        排序依据参数，取值如下： - certExpiredTime：证书到期时间。 - certStatus：证书状态。 - certUpdateTime：证书更新时间。

        :param sort_key: The sort_key of this ListCertificatesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListCertificatesRequest.

        证书状态，取值如下： - ALL：所有证书状态。 - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - CHECKING_ORG：待完成企业资格认证。 - ISSUING：证书待签发。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。

        :return: The status of this ListCertificatesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCertificatesRequest.

        证书状态，取值如下： - ALL：所有证书状态。 - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - CHECKING_ORG：待完成企业资格认证。 - ISSUING：证书待签发。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。

        :param status: The status of this ListCertificatesRequest.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCertificatesRequest.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCertificatesRequest.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this ListCertificatesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def deploy_support(self):
        """Gets the deploy_support of this ListCertificatesRequest.

        是否支持部署。

        :return: The deploy_support of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._deploy_support

    @deploy_support.setter
    def deploy_support(self, deploy_support):
        """Sets the deploy_support of this ListCertificatesRequest.

        是否支持部署。

        :param deploy_support: The deploy_support of this ListCertificatesRequest.
        :type deploy_support: bool
        """
        self._deploy_support = deploy_support

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
