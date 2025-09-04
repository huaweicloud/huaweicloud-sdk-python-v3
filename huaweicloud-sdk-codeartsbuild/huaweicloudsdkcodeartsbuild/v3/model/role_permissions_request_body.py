# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RolePermissionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'job_ids': 'list[str]',
        'project_switch': 'bool',
        'permissions': 'list[JobRolePermission]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'job_ids': 'job_ids',
        'project_switch': 'project_switch',
        'permissions': 'permissions'
    }

    def __init__(self, project_id=None, job_ids=None, project_switch=None, permissions=None):
        r"""RolePermissionsRequestBody

        The model defined in huaweicloud sdk

        :param project_id: CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。
        :type project_id: str
        :param job_ids: 任务id集合
        :type job_ids: list[str]
        :param project_switch: 是否同步最新项目权限
        :type project_switch: bool
        :param permissions: 角色权限信息
        :type permissions: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobRolePermission`]
        """
        
        

        self._project_id = None
        self._job_ids = None
        self._project_switch = None
        self._permissions = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if job_ids is not None:
            self.job_ids = job_ids
        if project_switch is not None:
            self.project_switch = project_switch
        if permissions is not None:
            self.permissions = permissions

    @property
    def project_id(self):
        r"""Gets the project_id of this RolePermissionsRequestBody.

        CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。

        :return: The project_id of this RolePermissionsRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RolePermissionsRequestBody.

        CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。

        :param project_id: The project_id of this RolePermissionsRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_ids(self):
        r"""Gets the job_ids of this RolePermissionsRequestBody.

        任务id集合

        :return: The job_ids of this RolePermissionsRequestBody.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        r"""Sets the job_ids of this RolePermissionsRequestBody.

        任务id集合

        :param job_ids: The job_ids of this RolePermissionsRequestBody.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

    @property
    def project_switch(self):
        r"""Gets the project_switch of this RolePermissionsRequestBody.

        是否同步最新项目权限

        :return: The project_switch of this RolePermissionsRequestBody.
        :rtype: bool
        """
        return self._project_switch

    @project_switch.setter
    def project_switch(self, project_switch):
        r"""Sets the project_switch of this RolePermissionsRequestBody.

        是否同步最新项目权限

        :param project_switch: The project_switch of this RolePermissionsRequestBody.
        :type project_switch: bool
        """
        self._project_switch = project_switch

    @property
    def permissions(self):
        r"""Gets the permissions of this RolePermissionsRequestBody.

        角色权限信息

        :return: The permissions of this RolePermissionsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobRolePermission`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this RolePermissionsRequestBody.

        角色权限信息

        :param permissions: The permissions of this RolePermissionsRequestBody.
        :type permissions: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobRolePermission`]
        """
        self._permissions = permissions

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
        if not isinstance(other, RolePermissionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
