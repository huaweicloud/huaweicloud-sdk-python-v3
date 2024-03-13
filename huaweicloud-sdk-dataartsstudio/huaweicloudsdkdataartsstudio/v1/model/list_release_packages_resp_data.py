# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReleasePackagesRespData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_timestamp': 'str',
        'apply_user_id': 'str',
        'apply_user_name': 'str',
        'delete_flag': 'int',
        'deploy_status': 'int',
        'deploy_timestamp': 'int',
        'deploy_user_id': 'str',
        'deploy_user_name': 'str',
        'package_approvers': 'list[ListReleasePackagesRespPackageApprovers]',
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
        """ListReleasePackagesRespData

        The model defined in huaweicloud sdk

        :param apply_timestamp: 申请时间，13位时间戳
        :type apply_timestamp: str
        :param apply_user_id: 申请人id
        :type apply_user_id: str
        :param apply_user_name: 申请人名称
        :type apply_user_name: str
        :param delete_flag: 是否删除，0:没有删除，1:删除
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
        :type package_approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespPackageApprovers`]
        :param package_id: 发布包id
        :type package_id: str
        :param package_name: 发布包名称
        :type package_name: str
        :param project_id: 项目ID和空间信息，以 项目ID-workspace-空间ID 拼接。
        :type project_id: str
        :param workspace_id: 发布包所在空间ID
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
        """Gets the apply_timestamp of this ListReleasePackagesRespData.

        申请时间，13位时间戳

        :return: The apply_timestamp of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._apply_timestamp

    @apply_timestamp.setter
    def apply_timestamp(self, apply_timestamp):
        """Sets the apply_timestamp of this ListReleasePackagesRespData.

        申请时间，13位时间戳

        :param apply_timestamp: The apply_timestamp of this ListReleasePackagesRespData.
        :type apply_timestamp: str
        """
        self._apply_timestamp = apply_timestamp

    @property
    def apply_user_id(self):
        """Gets the apply_user_id of this ListReleasePackagesRespData.

        申请人id

        :return: The apply_user_id of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, apply_user_id):
        """Sets the apply_user_id of this ListReleasePackagesRespData.

        申请人id

        :param apply_user_id: The apply_user_id of this ListReleasePackagesRespData.
        :type apply_user_id: str
        """
        self._apply_user_id = apply_user_id

    @property
    def apply_user_name(self):
        """Gets the apply_user_name of this ListReleasePackagesRespData.

        申请人名称

        :return: The apply_user_name of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._apply_user_name

    @apply_user_name.setter
    def apply_user_name(self, apply_user_name):
        """Sets the apply_user_name of this ListReleasePackagesRespData.

        申请人名称

        :param apply_user_name: The apply_user_name of this ListReleasePackagesRespData.
        :type apply_user_name: str
        """
        self._apply_user_name = apply_user_name

    @property
    def delete_flag(self):
        """Gets the delete_flag of this ListReleasePackagesRespData.

        是否删除，0:没有删除，1:删除

        :return: The delete_flag of this ListReleasePackagesRespData.
        :rtype: int
        """
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, delete_flag):
        """Sets the delete_flag of this ListReleasePackagesRespData.

        是否删除，0:没有删除，1:删除

        :param delete_flag: The delete_flag of this ListReleasePackagesRespData.
        :type delete_flag: int
        """
        self._delete_flag = delete_flag

    @property
    def deploy_status(self):
        """Gets the deploy_status of this ListReleasePackagesRespData.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :return: The deploy_status of this ListReleasePackagesRespData.
        :rtype: int
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this ListReleasePackagesRespData.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :param deploy_status: The deploy_status of this ListReleasePackagesRespData.
        :type deploy_status: int
        """
        self._deploy_status = deploy_status

    @property
    def deploy_timestamp(self):
        """Gets the deploy_timestamp of this ListReleasePackagesRespData.

        发布时间，13位时间戳

        :return: The deploy_timestamp of this ListReleasePackagesRespData.
        :rtype: int
        """
        return self._deploy_timestamp

    @deploy_timestamp.setter
    def deploy_timestamp(self, deploy_timestamp):
        """Sets the deploy_timestamp of this ListReleasePackagesRespData.

        发布时间，13位时间戳

        :param deploy_timestamp: The deploy_timestamp of this ListReleasePackagesRespData.
        :type deploy_timestamp: int
        """
        self._deploy_timestamp = deploy_timestamp

    @property
    def deploy_user_id(self):
        """Gets the deploy_user_id of this ListReleasePackagesRespData.

        发布人id

        :return: The deploy_user_id of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._deploy_user_id

    @deploy_user_id.setter
    def deploy_user_id(self, deploy_user_id):
        """Sets the deploy_user_id of this ListReleasePackagesRespData.

        发布人id

        :param deploy_user_id: The deploy_user_id of this ListReleasePackagesRespData.
        :type deploy_user_id: str
        """
        self._deploy_user_id = deploy_user_id

    @property
    def deploy_user_name(self):
        """Gets the deploy_user_name of this ListReleasePackagesRespData.

        发布人名称

        :return: The deploy_user_name of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._deploy_user_name

    @deploy_user_name.setter
    def deploy_user_name(self, deploy_user_name):
        """Sets the deploy_user_name of this ListReleasePackagesRespData.

        发布人名称

        :param deploy_user_name: The deploy_user_name of this ListReleasePackagesRespData.
        :type deploy_user_name: str
        """
        self._deploy_user_name = deploy_user_name

    @property
    def package_approvers(self):
        """Gets the package_approvers of this ListReleasePackagesRespData.

        发布包审批信息

        :return: The package_approvers of this ListReleasePackagesRespData.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespPackageApprovers`]
        """
        return self._package_approvers

    @package_approvers.setter
    def package_approvers(self, package_approvers):
        """Sets the package_approvers of this ListReleasePackagesRespData.

        发布包审批信息

        :param package_approvers: The package_approvers of this ListReleasePackagesRespData.
        :type package_approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespPackageApprovers`]
        """
        self._package_approvers = package_approvers

    @property
    def package_id(self):
        """Gets the package_id of this ListReleasePackagesRespData.

        发布包id

        :return: The package_id of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ListReleasePackagesRespData.

        发布包id

        :param package_id: The package_id of this ListReleasePackagesRespData.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def package_name(self):
        """Gets the package_name of this ListReleasePackagesRespData.

        发布包名称

        :return: The package_name of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ListReleasePackagesRespData.

        发布包名称

        :param package_name: The package_name of this ListReleasePackagesRespData.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def project_id(self):
        """Gets the project_id of this ListReleasePackagesRespData.

        项目ID和空间信息，以 项目ID-workspace-空间ID 拼接。

        :return: The project_id of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListReleasePackagesRespData.

        项目ID和空间信息，以 项目ID-workspace-空间ID 拼接。

        :param project_id: The project_id of this ListReleasePackagesRespData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListReleasePackagesRespData.

        发布包所在空间ID

        :return: The workspace_id of this ListReleasePackagesRespData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListReleasePackagesRespData.

        发布包所在空间ID

        :param workspace_id: The workspace_id of this ListReleasePackagesRespData.
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
        if not isinstance(other, ListReleasePackagesRespData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
