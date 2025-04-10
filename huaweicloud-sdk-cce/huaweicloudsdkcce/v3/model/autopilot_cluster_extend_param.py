# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutopilotClusterExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'upgradefrom': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterpriseProjectId',
        'upgradefrom': 'upgradefrom'
    }

    def __init__(self, enterprise_project_id=None, upgradefrom=None):
        r"""AutopilotClusterExtendParam

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 集群所属的企业项目ID。 &gt;   - 需要开通企业项目功能后才可配置企业项目。 &gt;   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 
        :type enterprise_project_id: str
        :param upgradefrom: 记录集群通过何种升级方式升级到当前版本。 
        :type upgradefrom: str
        """
        
        

        self._enterprise_project_id = None
        self._upgradefrom = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if upgradefrom is not None:
            self.upgradefrom = upgradefrom

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AutopilotClusterExtendParam.

        集群所属的企业项目ID。 >   - 需要开通企业项目功能后才可配置企业项目。 >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 

        :return: The enterprise_project_id of this AutopilotClusterExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AutopilotClusterExtendParam.

        集群所属的企业项目ID。 >   - 需要开通企业项目功能后才可配置企业项目。 >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 

        :param enterprise_project_id: The enterprise_project_id of this AutopilotClusterExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def upgradefrom(self):
        r"""Gets the upgradefrom of this AutopilotClusterExtendParam.

        记录集群通过何种升级方式升级到当前版本。 

        :return: The upgradefrom of this AutopilotClusterExtendParam.
        :rtype: str
        """
        return self._upgradefrom

    @upgradefrom.setter
    def upgradefrom(self, upgradefrom):
        r"""Sets the upgradefrom of this AutopilotClusterExtendParam.

        记录集群通过何种升级方式升级到当前版本。 

        :param upgradefrom: The upgradefrom of this AutopilotClusterExtendParam.
        :type upgradefrom: str
        """
        self._upgradefrom = upgradefrom

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
        if not isinstance(other, AutopilotClusterExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
