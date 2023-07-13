# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableDisasterClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_cluster_id': 'str',
        'primary_spec_id': 'str',
        'primary_cluster_dn_num': 'str',
        'standby_region': 'str',
        'standby_project_id': 'str',
        'standby_az_code': 'str',
        'dr_type': 'str',
        'datastore_type': 'str',
        'datastore_version': 'str'
    }

    attribute_map = {
        'primary_cluster_id': 'primary_cluster_id',
        'primary_spec_id': 'primary_spec_id',
        'primary_cluster_dn_num': 'primary_cluster_dn_num',
        'standby_region': 'standby_region',
        'standby_project_id': 'standby_project_id',
        'standby_az_code': 'standby_az_code',
        'dr_type': 'dr_type',
        'datastore_type': 'datastore_type',
        'datastore_version': 'datastore_version'
    }

    def __init__(self, primary_cluster_id=None, primary_spec_id=None, primary_cluster_dn_num=None, standby_region=None, standby_project_id=None, standby_az_code=None, dr_type=None, datastore_type=None, datastore_version=None):
        """ListAvailableDisasterClustersRequest

        The model defined in huaweicloud sdk

        :param primary_cluster_id: 主集群ID
        :type primary_cluster_id: str
        :param primary_spec_id: 主集群规格ID
        :type primary_spec_id: str
        :param primary_cluster_dn_num: 主集群DN数量
        :type primary_cluster_dn_num: str
        :param standby_region: 备集群所在region
        :type standby_region: str
        :param standby_project_id: 备集群项目ID
        :type standby_project_id: str
        :param standby_az_code: 备集群所在AZ
        :type standby_az_code: str
        :param dr_type: 容灾类型
        :type dr_type: str
        :param datastore_type: 数仓类型
        :type datastore_type: str
        :param datastore_version: 数仓版本
        :type datastore_version: str
        """
        
        

        self._primary_cluster_id = None
        self._primary_spec_id = None
        self._primary_cluster_dn_num = None
        self._standby_region = None
        self._standby_project_id = None
        self._standby_az_code = None
        self._dr_type = None
        self._datastore_type = None
        self._datastore_version = None
        self.discriminator = None

        self.primary_cluster_id = primary_cluster_id
        if primary_spec_id is not None:
            self.primary_spec_id = primary_spec_id
        if primary_cluster_dn_num is not None:
            self.primary_cluster_dn_num = primary_cluster_dn_num
        if standby_region is not None:
            self.standby_region = standby_region
        if standby_project_id is not None:
            self.standby_project_id = standby_project_id
        self.standby_az_code = standby_az_code
        if dr_type is not None:
            self.dr_type = dr_type
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if datastore_version is not None:
            self.datastore_version = datastore_version

    @property
    def primary_cluster_id(self):
        """Gets the primary_cluster_id of this ListAvailableDisasterClustersRequest.

        主集群ID

        :return: The primary_cluster_id of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._primary_cluster_id

    @primary_cluster_id.setter
    def primary_cluster_id(self, primary_cluster_id):
        """Sets the primary_cluster_id of this ListAvailableDisasterClustersRequest.

        主集群ID

        :param primary_cluster_id: The primary_cluster_id of this ListAvailableDisasterClustersRequest.
        :type primary_cluster_id: str
        """
        self._primary_cluster_id = primary_cluster_id

    @property
    def primary_spec_id(self):
        """Gets the primary_spec_id of this ListAvailableDisasterClustersRequest.

        主集群规格ID

        :return: The primary_spec_id of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._primary_spec_id

    @primary_spec_id.setter
    def primary_spec_id(self, primary_spec_id):
        """Sets the primary_spec_id of this ListAvailableDisasterClustersRequest.

        主集群规格ID

        :param primary_spec_id: The primary_spec_id of this ListAvailableDisasterClustersRequest.
        :type primary_spec_id: str
        """
        self._primary_spec_id = primary_spec_id

    @property
    def primary_cluster_dn_num(self):
        """Gets the primary_cluster_dn_num of this ListAvailableDisasterClustersRequest.

        主集群DN数量

        :return: The primary_cluster_dn_num of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._primary_cluster_dn_num

    @primary_cluster_dn_num.setter
    def primary_cluster_dn_num(self, primary_cluster_dn_num):
        """Sets the primary_cluster_dn_num of this ListAvailableDisasterClustersRequest.

        主集群DN数量

        :param primary_cluster_dn_num: The primary_cluster_dn_num of this ListAvailableDisasterClustersRequest.
        :type primary_cluster_dn_num: str
        """
        self._primary_cluster_dn_num = primary_cluster_dn_num

    @property
    def standby_region(self):
        """Gets the standby_region of this ListAvailableDisasterClustersRequest.

        备集群所在region

        :return: The standby_region of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._standby_region

    @standby_region.setter
    def standby_region(self, standby_region):
        """Sets the standby_region of this ListAvailableDisasterClustersRequest.

        备集群所在region

        :param standby_region: The standby_region of this ListAvailableDisasterClustersRequest.
        :type standby_region: str
        """
        self._standby_region = standby_region

    @property
    def standby_project_id(self):
        """Gets the standby_project_id of this ListAvailableDisasterClustersRequest.

        备集群项目ID

        :return: The standby_project_id of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._standby_project_id

    @standby_project_id.setter
    def standby_project_id(self, standby_project_id):
        """Sets the standby_project_id of this ListAvailableDisasterClustersRequest.

        备集群项目ID

        :param standby_project_id: The standby_project_id of this ListAvailableDisasterClustersRequest.
        :type standby_project_id: str
        """
        self._standby_project_id = standby_project_id

    @property
    def standby_az_code(self):
        """Gets the standby_az_code of this ListAvailableDisasterClustersRequest.

        备集群所在AZ

        :return: The standby_az_code of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._standby_az_code

    @standby_az_code.setter
    def standby_az_code(self, standby_az_code):
        """Sets the standby_az_code of this ListAvailableDisasterClustersRequest.

        备集群所在AZ

        :param standby_az_code: The standby_az_code of this ListAvailableDisasterClustersRequest.
        :type standby_az_code: str
        """
        self._standby_az_code = standby_az_code

    @property
    def dr_type(self):
        """Gets the dr_type of this ListAvailableDisasterClustersRequest.

        容灾类型

        :return: The dr_type of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        """Sets the dr_type of this ListAvailableDisasterClustersRequest.

        容灾类型

        :param dr_type: The dr_type of this ListAvailableDisasterClustersRequest.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ListAvailableDisasterClustersRequest.

        数仓类型

        :return: The datastore_type of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ListAvailableDisasterClustersRequest.

        数仓类型

        :param datastore_type: The datastore_type of this ListAvailableDisasterClustersRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def datastore_version(self):
        """Gets the datastore_version of this ListAvailableDisasterClustersRequest.

        数仓版本

        :return: The datastore_version of this ListAvailableDisasterClustersRequest.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        """Sets the datastore_version of this ListAvailableDisasterClustersRequest.

        数仓版本

        :param datastore_version: The datastore_version of this ListAvailableDisasterClustersRequest.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

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
        if not isinstance(other, ListAvailableDisasterClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
