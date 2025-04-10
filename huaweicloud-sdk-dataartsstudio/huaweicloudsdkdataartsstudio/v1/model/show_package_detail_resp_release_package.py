# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPackageDetailRespReleasePackage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_timestamp': 'int',
        'apply_user_id': 'str',
        'apply_user_name': 'str',
        'delete_flag': 'int',
        'deploy_status': 'int',
        'deploy_timestamp': 'int',
        'deploy_user_id': 'str',
        'deploy_user_name': 'str',
        'package_approvers': 'list[ShowPackageDetailRespReleasePackagePackageApprovers]',
        'package_id': 'str',
        'package_name': 'str',
        'project_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'apply_timestamp': 'apply_timestamp',
        'apply_user_id': 'apply_user_id',
        'apply_user_name': 'apply_user_name',
        'delete_flag': 'delete_flag',
        'deploy_status': 'deploy_status',
        'deploy_timestamp': 'deploy_timestamp',
        'deploy_user_id': 'deploy_user_id',
        'deploy_user_name': 'deploy_user_name',
        'package_approvers': 'package_approvers',
        'package_id': 'package_id',
        'package_name': 'package_name',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, apply_timestamp=None, apply_user_id=None, apply_user_name=None, delete_flag=None, deploy_status=None, deploy_timestamp=None, deploy_user_id=None, deploy_user_name=None, package_approvers=None, package_id=None, package_name=None, project_id=None, workspace_id=None):
        r"""ShowPackageDetailRespReleasePackage

        The model defined in huaweicloud sdk

        :param apply_timestamp: 申请时间，13位时间戳
        :type apply_timestamp: int
        :param apply_user_id: 申请id
        :type apply_user_id: str
        :param apply_user_name: 申请人名称
        :type apply_user_name: str
        :param delete_flag: 是否删除，0:不删除，1:不删除
        :type delete_flag: int
        :param deploy_status: 发布状态，1:待审批,2:成功,3:失败, 5:发布中
        :type deploy_status: int
        :param deploy_timestamp: 发布时间，13位时间戳
        :type deploy_timestamp: int
        :param deploy_user_id: 发布人id
        :type deploy_user_id: str
        :param deploy_user_name: 发布人名称
        :type deploy_user_name: str
        :param package_approvers: 发布包审批信息
        :type package_approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackagePackageApprovers`]
        :param package_id: 发布包id
        :type package_id: str
        :param package_name: 发布包名称
        :type package_name: str
        :param project_id: 项目ID+workspace+workspaceId
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._apply_timestamp = None
        self._apply_user_id = None
        self._apply_user_name = None
        self._delete_flag = None
        self._deploy_status = None
        self._deploy_timestamp = None
        self._deploy_user_id = None
        self._deploy_user_name = None
        self._package_approvers = None
        self._package_id = None
        self._package_name = None
        self._project_id = None
        self._workspace_id = None
        self.discriminator = None

        if apply_timestamp is not None:
            self.apply_timestamp = apply_timestamp
        if apply_user_id is not None:
            self.apply_user_id = apply_user_id
        if apply_user_name is not None:
            self.apply_user_name = apply_user_name
        if delete_flag is not None:
            self.delete_flag = delete_flag
        if deploy_status is not None:
            self.deploy_status = deploy_status
        if deploy_timestamp is not None:
            self.deploy_timestamp = deploy_timestamp
        if deploy_user_id is not None:
            self.deploy_user_id = deploy_user_id
        if deploy_user_name is not None:
            self.deploy_user_name = deploy_user_name
        self.package_approvers = package_approvers
        if package_id is not None:
            self.package_id = package_id
        if package_name is not None:
            self.package_name = package_name
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def apply_timestamp(self):
        r"""Gets the apply_timestamp of this ShowPackageDetailRespReleasePackage.

        申请时间，13位时间戳

        :return: The apply_timestamp of this ShowPackageDetailRespReleasePackage.
        :rtype: int
        """
        return self._apply_timestamp

    @apply_timestamp.setter
    def apply_timestamp(self, apply_timestamp):
        r"""Sets the apply_timestamp of this ShowPackageDetailRespReleasePackage.

        申请时间，13位时间戳

        :param apply_timestamp: The apply_timestamp of this ShowPackageDetailRespReleasePackage.
        :type apply_timestamp: int
        """
        self._apply_timestamp = apply_timestamp

    @property
    def apply_user_id(self):
        r"""Gets the apply_user_id of this ShowPackageDetailRespReleasePackage.

        申请id

        :return: The apply_user_id of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, apply_user_id):
        r"""Sets the apply_user_id of this ShowPackageDetailRespReleasePackage.

        申请id

        :param apply_user_id: The apply_user_id of this ShowPackageDetailRespReleasePackage.
        :type apply_user_id: str
        """
        self._apply_user_id = apply_user_id

    @property
    def apply_user_name(self):
        r"""Gets the apply_user_name of this ShowPackageDetailRespReleasePackage.

        申请人名称

        :return: The apply_user_name of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._apply_user_name

    @apply_user_name.setter
    def apply_user_name(self, apply_user_name):
        r"""Sets the apply_user_name of this ShowPackageDetailRespReleasePackage.

        申请人名称

        :param apply_user_name: The apply_user_name of this ShowPackageDetailRespReleasePackage.
        :type apply_user_name: str
        """
        self._apply_user_name = apply_user_name

    @property
    def delete_flag(self):
        r"""Gets the delete_flag of this ShowPackageDetailRespReleasePackage.

        是否删除，0:不删除，1:不删除

        :return: The delete_flag of this ShowPackageDetailRespReleasePackage.
        :rtype: int
        """
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, delete_flag):
        r"""Sets the delete_flag of this ShowPackageDetailRespReleasePackage.

        是否删除，0:不删除，1:不删除

        :param delete_flag: The delete_flag of this ShowPackageDetailRespReleasePackage.
        :type delete_flag: int
        """
        self._delete_flag = delete_flag

    @property
    def deploy_status(self):
        r"""Gets the deploy_status of this ShowPackageDetailRespReleasePackage.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :return: The deploy_status of this ShowPackageDetailRespReleasePackage.
        :rtype: int
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        r"""Sets the deploy_status of this ShowPackageDetailRespReleasePackage.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :param deploy_status: The deploy_status of this ShowPackageDetailRespReleasePackage.
        :type deploy_status: int
        """
        self._deploy_status = deploy_status

    @property
    def deploy_timestamp(self):
        r"""Gets the deploy_timestamp of this ShowPackageDetailRespReleasePackage.

        发布时间，13位时间戳

        :return: The deploy_timestamp of this ShowPackageDetailRespReleasePackage.
        :rtype: int
        """
        return self._deploy_timestamp

    @deploy_timestamp.setter
    def deploy_timestamp(self, deploy_timestamp):
        r"""Sets the deploy_timestamp of this ShowPackageDetailRespReleasePackage.

        发布时间，13位时间戳

        :param deploy_timestamp: The deploy_timestamp of this ShowPackageDetailRespReleasePackage.
        :type deploy_timestamp: int
        """
        self._deploy_timestamp = deploy_timestamp

    @property
    def deploy_user_id(self):
        r"""Gets the deploy_user_id of this ShowPackageDetailRespReleasePackage.

        发布人id

        :return: The deploy_user_id of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._deploy_user_id

    @deploy_user_id.setter
    def deploy_user_id(self, deploy_user_id):
        r"""Sets the deploy_user_id of this ShowPackageDetailRespReleasePackage.

        发布人id

        :param deploy_user_id: The deploy_user_id of this ShowPackageDetailRespReleasePackage.
        :type deploy_user_id: str
        """
        self._deploy_user_id = deploy_user_id

    @property
    def deploy_user_name(self):
        r"""Gets the deploy_user_name of this ShowPackageDetailRespReleasePackage.

        发布人名称

        :return: The deploy_user_name of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._deploy_user_name

    @deploy_user_name.setter
    def deploy_user_name(self, deploy_user_name):
        r"""Sets the deploy_user_name of this ShowPackageDetailRespReleasePackage.

        发布人名称

        :param deploy_user_name: The deploy_user_name of this ShowPackageDetailRespReleasePackage.
        :type deploy_user_name: str
        """
        self._deploy_user_name = deploy_user_name

    @property
    def package_approvers(self):
        r"""Gets the package_approvers of this ShowPackageDetailRespReleasePackage.

        发布包审批信息

        :return: The package_approvers of this ShowPackageDetailRespReleasePackage.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackagePackageApprovers`]
        """
        return self._package_approvers

    @package_approvers.setter
    def package_approvers(self, package_approvers):
        r"""Sets the package_approvers of this ShowPackageDetailRespReleasePackage.

        发布包审批信息

        :param package_approvers: The package_approvers of this ShowPackageDetailRespReleasePackage.
        :type package_approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackagePackageApprovers`]
        """
        self._package_approvers = package_approvers

    @property
    def package_id(self):
        r"""Gets the package_id of this ShowPackageDetailRespReleasePackage.

        发布包id

        :return: The package_id of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this ShowPackageDetailRespReleasePackage.

        发布包id

        :param package_id: The package_id of this ShowPackageDetailRespReleasePackage.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def package_name(self):
        r"""Gets the package_name of this ShowPackageDetailRespReleasePackage.

        发布包名称

        :return: The package_name of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this ShowPackageDetailRespReleasePackage.

        发布包名称

        :param package_name: The package_name of this ShowPackageDetailRespReleasePackage.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPackageDetailRespReleasePackage.

        项目ID+workspace+workspaceId

        :return: The project_id of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPackageDetailRespReleasePackage.

        项目ID+workspace+workspaceId

        :param project_id: The project_id of this ShowPackageDetailRespReleasePackage.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowPackageDetailRespReleasePackage.

        工作空间ID

        :return: The workspace_id of this ShowPackageDetailRespReleasePackage.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowPackageDetailRespReleasePackage.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowPackageDetailRespReleasePackage.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ShowPackageDetailRespReleasePackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
