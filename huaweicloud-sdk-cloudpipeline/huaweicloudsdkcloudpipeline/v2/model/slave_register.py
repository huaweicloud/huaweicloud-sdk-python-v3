# coding: utf-8

import pprint
import re

import six





class SlaveRegister:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'slave_name': 'str',
        'work_dir': 'str',
        'label': 'str',
        'version': 'str',
        'retry': 'bool',
        'owner_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'slave_name': 'slave_name',
        'work_dir': 'work_dir',
        'label': 'label',
        'version': 'version',
        'retry': 'retry',
        'owner_type': 'owner_type'
    }

    def __init__(self, cluster_id=None, slave_name=None, work_dir=None, label=None, version=None, retry=False, owner_type='customer'):
        """SlaveRegister - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._slave_name = None
        self._work_dir = None
        self._label = None
        self._version = None
        self._retry = None
        self._owner_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.slave_name = slave_name
        self.work_dir = work_dir
        if label is not None:
            self.label = label
        if version is not None:
            self.version = version
        if retry is not None:
            self.retry = retry
        if owner_type is not None:
            self.owner_type = owner_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SlaveRegister.

        cluster ID

        :return: The cluster_id of this SlaveRegister.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SlaveRegister.

        cluster ID

        :param cluster_id: The cluster_id of this SlaveRegister.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def slave_name(self):
        """Gets the slave_name of this SlaveRegister.

        Slave名称

        :return: The slave_name of this SlaveRegister.
        :rtype: str
        """
        return self._slave_name

    @slave_name.setter
    def slave_name(self, slave_name):
        """Sets the slave_name of this SlaveRegister.

        Slave名称

        :param slave_name: The slave_name of this SlaveRegister.
        :type: str
        """
        self._slave_name = slave_name

    @property
    def work_dir(self):
        """Gets the work_dir of this SlaveRegister.

        Slave工作空间

        :return: The work_dir of this SlaveRegister.
        :rtype: str
        """
        return self._work_dir

    @work_dir.setter
    def work_dir(self, work_dir):
        """Sets the work_dir of this SlaveRegister.

        Slave工作空间

        :param work_dir: The work_dir of this SlaveRegister.
        :type: str
        """
        self._work_dir = work_dir

    @property
    def label(self):
        """Gets the label of this SlaveRegister.

        Slave label

        :return: The label of this SlaveRegister.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SlaveRegister.

        Slave label

        :param label: The label of this SlaveRegister.
        :type: str
        """
        self._label = label

    @property
    def version(self):
        """Gets the version of this SlaveRegister.

        agent版本

        :return: The version of this SlaveRegister.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SlaveRegister.

        agent版本

        :param version: The version of this SlaveRegister.
        :type: str
        """
        self._version = version

    @property
    def retry(self):
        """Gets the retry of this SlaveRegister.

        是否重试

        :return: The retry of this SlaveRegister.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this SlaveRegister.

        是否重试

        :param retry: The retry of this SlaveRegister.
        :type: bool
        """
        self._retry = retry

    @property
    def owner_type(self):
        """Gets the owner_type of this SlaveRegister.

        Slave ownerType

        :return: The owner_type of this SlaveRegister.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this SlaveRegister.

        Slave ownerType

        :param owner_type: The owner_type of this SlaveRegister.
        :type: str
        """
        self._owner_type = owner_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlaveRegister):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
